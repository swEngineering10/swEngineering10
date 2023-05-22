import pygame
import pygame.freetype
import pygame_gui
import json
import sys
from pygame.surface import Surface
from pygame.event import Event
from pygame_gui.elements.ui_button import UIButton
from pygame.locals import *
from utility import resolution
from client.networking import Networking
from screens.abc_screen import Screen
from screens.lobby_screen import LobbyScreen
from screens.map_screen import MapScreen
from network_server import Server


class Password(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        self.screen_width, self.screen_height = resolution()
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        with open('keys.json', 'r') as f:
            keyboard_data = json.load(f)

        self.key_up = keyboard_data["1073741906"]
        self.key_down = keyboard_data["1073741905"]

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.next_screen = Server

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.font = pygame.font.Font(None, 48)

        # 입력 상자 생성
        input_box_width = 400
        input_box_height = 64
        self.password_box = pygame.Rect(
            self.screen_width // 2 - input_box_width // 2,
            self.screen_height // 2 - input_box_height // 2,
            input_box_width,
            input_box_height,
        )
        self.password = ''

        # OK 버튼
        button_width = 200
        button_height = 64
        self.OK_button = pygame.Rect(
            self.screen_width // 2 - button_width // 2,
            self.screen_height // 2 + 100,
            button_width,
            button_height,
        )

        self.password_file = "password.json"

    def save_password(self):
        data = {"password": self.password}
        with open(self.password_file, "w") as f:
            json.dump(data, f)

    def handle_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if self.password_box.collidepoint(pygame.mouse.get_pos()):
                    self.password = self.password[:-1]
            else:
                if self.password_box.collidepoint(pygame.mouse.get_pos()):
                    self.password += event.unicode
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.OK_button.collidepoint(mouse_pos):
                # 비밀번호를 JSON 파일에 저장
                self.save_password()
                # server에 password 전달
                self.next_screen = Server
                self.is_running = False

    def run(self, events: list[Event]) -> bool:
        self.screen.fill(self.WHITE)

        # Create a password 표시하기
        password_text = self.font.render("Create a password", True, self.BLACK)
        password_text_rect = password_text.get_rect(
            center=(self.screen_width // 2, self.screen_height // 2 - 100)
        )
        self.screen.blit(password_text, password_text_rect)

        # 비밀번호 입력 상자 그리기
        pygame.draw.rect(self.screen, self.BLACK, self.password_box, 2)
        self.password_surface = self.font.render(
            self.password, True, self.BLACK)
        password_surface_rect = self.password_surface.get_rect(
            center=(self.password_box.x + self.password_box.width // 2,
                    self.password_box.y + self.password_box.height // 2)
        )
        self.screen.blit(self.password_surface, password_surface_rect)

        # OK 버튼 그리기
        pygame.draw.rect(self.screen, self.BLACK, self.OK_button)
        button_text = self.font.render('OK', True, self.WHITE)
        button_text_rect = button_text.get_rect(
            center=(self.OK_button.x + self.OK_button.width // 2,
                    self.OK_button.y + self.OK_button.height // 2)
        )
        self.screen.blit(button_text, button_text_rect)

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running
