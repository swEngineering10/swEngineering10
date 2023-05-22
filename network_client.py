import pygame
import pygame_gui
from pygame.locals import *
import socket
import pickle
import sys

from pygame.event import Event
from pygame.surface import Surface

from screens.abc_screen import Screen
from client.networking import Networking
from screens.lobby_screen import LobbyScreen


class Client(Screen):
    def __init__(self, surface: Surface,  manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        self.screen_width, self.screen_height = 400, 300
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.next_screen = LobbyScreen

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.font = pygame.font.Font(None, 32)

        # 입력 상자 생성
        self.input_box = pygame.Rect(50, 100, 200, 32)
        self.input_text = ''

        # 사용자 이름 입력 상자 생성
        self.username_box = pygame.Rect(50, 50, 200, 32)
        self.username_text = ''

        # 버튼 생성
        self.connect_button = pygame.Rect(50, 200, 100, 50)

        # 서버 정보를 저장할 변수 초기화
        self.server_info_text = ''

        # 서버 주소 초기화
        self.server_address = ''
        self.received_password = ''
        self.password = ''

        self.connected = False
        self.show_password_box = False
        self.password_text = ''

    def receive_json_file(self, socekt, filename):
        try:
            with open(filename, "wb") as f:
                while True:
                    data = socekt.recv(1024)
                    if not data:
                        break
                    f.write(data)
        except OSError as e:
            print("파일 수신 오류: ", e)

    def handle_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if self.input_box.collidepoint(pygame.mouse.get_pos()):
                    self.input_text = self.input_text[:-1]
                elif self.show_password_box:
                    self.password_text = self.password_text[:-1]
                elif self.username_box.collidepoint(pygame.mouse.get_pos()):
                    self.username_text = self.username_text[:-1]
            else:
                if self.input_box.collidepoint(pygame.mouse.get_pos()):
                    self.input_text += event.unicode
                elif self.show_password_box:
                    self.password_text += event.unicode
                elif self.username_box.collidepoint(pygame.mouse.get_pos()):
                    self.username_text += event.unicode
        elif event.type == MOUSEBUTTONDOWN:
            self.mouse_pos = pygame.mouse.get_pos()
            if self.connect_button.collidepoint(self.mouse_pos):
                if not self.connected:
                    # 서버로 ip 주소 전송
                    if self.input_text:
                        self.server_address = self.input_text

                        # 서버에 연결
                        self.client_socket = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
                        self.client_socket.connect((self.server_address, 5557))

                    if self.username_text:
                        self.username = self.username_text
                        self.client_socket.sendall(self.username.encode())

                    self.show_password_box = True

                elif self.show_password_box:
                    # 서버로부터 password.json 파일 수신
                    self.receive_json_file(self.client_socket, "password.json")

                    # password.json 파일 열고 내용 출력
                    try:
                        with open("password.json", "r") as f:
                            password_data = self.json.load(f)
                            print("Received password data: ", password_data)
                    except FileNotFoundError:
                        print("Falied to open password.json file")

                    # 서버로 비밀번호 전송
                    if self.password_text:
                        self.password = self.password_text

                        # 비밀번호를 서버로 전송
                        try:
                            self.client_socket.sendall(self.password.encode())
                        except OSError as e:
                            print("소켓 작업 오류 발생:", e)

                        # 서버 응답 받기
                        try:
                            self.response = self.client_socket.recv(
                                1024).decode()
                        except OSError as e:
                            print("소켓 작업 오류 발생:", e)
                        if self.response == "Connect":
                            print("로비에 접속되었습니다.")
                            self.server_info_data = pickle.loads(
                                self.client_socket.recv(1024))
                            self.server_name = self.server_info_data['server_name']
                            self.server_address = self.server_info_data['server_address']
                            print('서버 정보 -이름:', self.server_name,
                                  '주소:', self.server_address)
                            self.next_screen = LobbyScreen
                            self.is_running = False
                        else:
                            print("비밀번호가 틀렸습니다.")

                        # 클라이언트 소켓 종료
                        self.client_socket.close()

    def run(self, events: list[Event]) -> bool:
        self.screen.fill(self.WHITE)

        # 서버의 IP 주소 표시하기
        SERVER_IP = '10.50.47.141'
        server_ip_text = self.font.render(
            "Server's IP address: " + SERVER_IP, True, self.BLACK)
        self.screen.blit(server_ip_text, (10, 10))

        # 사용자 이름 입력 상자 그리기
        pygame.draw.rect(self.screen, self.BLACK, self.username_box, 2)
        self.username_surface = self.font.render(
            self.username_text, True, self.BLACK)
        self.screen.blit(self.username_surface,
                         (self.username_box.x + 5, self.username_box.y + 5))

        # 입력 상자 그리기
        pygame.draw.rect(self.screen, self.BLACK, self.input_box, 2)
        self.input_surface = self.font.render(
            self.input_text, True, self.BLACK)
        self.screen.blit(self.input_surface,
                         (self.input_box.x + 5, self.input_box.y + 5))

        # 버튼 그리기
        pygame.draw.rect(self.screen, self.BLACK, self.connect_button)
        self.button_text = self.font.render('Connect', True, self.WHITE)
        self.screen.blit(
            self.button_text, (self.connect_button.x + 10, self.connect_button.y + 10))

        # 비밀번호 상자 그리기
        if self.show_password_box:
            self.password_box = pygame.Rect(50, 150, 200, 32)
            pygame.draw.rect(self.screen, self.BLACK, self.password_box, 2)
            self.password_surface = self.font.render(
                '*' * len(self.password_text), True, self.BLACK)
            self.screen.blit(self.password_surface,
                             (self.password_box.x + 5, self.password_box.y + 5))

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running
