import pygame
import pygame_gui
from pygame.locals import *
import socket
import pickle
import sys
import json

from pygame.event import Event
from pygame.surface import Surface

from screens.abc_screen import Screen
from client.networking import Networking
from screens.lobby_screen import LobbyScreen
from screens.server_lobby import ServerLobby


class Server(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)
        self.screen_width, self.screen_height = 400, 300
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE
        self.next_screen = ServerLobby
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # 네모난 박스 생성
        self.box_rect = pygame.Rect(50, 50, 100, 100)

        # 서버 주소와 이름, 비밀번호 설정
        self.server_name = 'team'
        self.server_address = '10.50.47.150'
        # self.password = '1234'
        self.password = ''
        self.password_file = "password.json"
        self.load_password()

        # 서버 소켓 생성 및 연결 대기
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_address, 5557))
        self.server_socket.listen(1)

        print('서버가 시작되었습니다. 클라이언트의 연결을 기다립니다. 비밀번호: ' + self.password)

        self.connected = False
        self.client_address = ''
        self.received_password = ''

        # 네모난 박스 상태
        self.box_state = False

        self.client_name = ''
        self.client_ip = ''

        # Start 버튼 생성
        self.start_button = pygame.Rect(150, 200, 100, 50)

    def load_password(self):
        with open(self.password_file, "r") as f:
            data = json.load(f)
            self.password = data.get("password", "")

    def send_json_file(self, client_socket, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            json_data = json.dumps(data)
            client_socket.sendall(json_data.encode())

    def handle_event(self, event):
        if not self.connected:
            # 클라이언트 연결 수락
            self.client_socket, self.client_address = self.server_socket.accept()
            print('새로운 클라이언트가 연결되었습니다:', self.client_address)

            # 사용자 이름 수신
            self.username = self.client_socket.recv(1024).decode()
            print('클라이언트 이름: ', self.username)

            # 클라이언트에게 비밀번호 전송
            # self.client_socket.sendall(self.password.encode())

            # 클라이언트로부터 비밀번호 수신
            self.received_password = self.client_socket.recv(1024).decode()

            # 비밀번호 확인
            if self.received_password == self.password:
                self.connected = True
                print('비밀번호가 일치하여 클라이언트와 연결되었습니다.')
                self.response = "Connect"
                self.client_socket.sendall(self.response.encode())
            else:
                print("비밀번호가 틀렸습니다. 클라이언트 연결 거부.")
                self.response = "Invalid"
                self.client_socket.sendall(self.response.encode())

            self.server_info_data = {
                'server_name': self.server_name, 'server_address': self.server_address}
            self.client_socket.sendall(pickle.dumps(self.server_info_data))

            # 클라이언트에게 json 파일 전송
            self.send_json_file(self.client_socket, "password.json")

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                if self.start_button.collidepoint(self.mouse_pos):
                    if self.connected:
                        print('Start 버튼이 클릭되었습니다.')
                        print('게임에 연결합니다.')

    def set_password(self, password):
        self.password = password

    def run(self, events: list[Event]) -> bool:
        self.screen.fill(self.WHITE)

        if self.connected:
            self.font = pygame.font.Font(None, 24)
            self.name_text = self.font.render(
                'Client Name: ' + self.client_name, True, self.BLACK)
            self.ip_text = self.font.render(
                'IP Address: ' + self.client_ip, True, self.BLACK)
            self.screen.blit(self.name_text, (10, 10))
            self.screen.blit(self.ip_text, (10, 30))

            pygame.draw.rect(self.screen, self.BLACK, self.start_button)
            self.button_text = self.font.render('Start', True, self.WHITE)
            self.screen.blit(
                self.button_text, (self.start_button.x + 25, self.start_button.y + 15))

        for event in events:
            self.handle_event(event)

    # def get_client_socket(self):
    #     return self.client_socket

        pygame.display.flip()
