import pygame
import pygame.freetype
import pygame_gui
import json
from pygame.surface import Surface
from pygame.event import Event
from pygame_gui.elements.ui_button import UIButton

from client.networking import Networking
from screens.abc_screen import Screen
from screens.lobby_screen import LobbyScreen
from screens.map_screen import MapScreen

class ModeScreen(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        # json 파일 로드
        with open('display_config.json', 'r') as f:
            config_data = json.load(f)

        # json 파일로부터 받은 해상도 값 반영
        self.screen_width = config_data['resolution']['width']
        self.screen_height = config_data['resolution']['height']
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE

        # Select Mode 텍스트
        self.font = pygame.font.SysFont(None, 80)
        self.text = self.font.render("Select Mode", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.screen_width//2, self.screen_height*0.3))

        # 버튼 생성
        self.normal_mode_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            self.screen_width // 2 - 100, self.screen_height // 2, 200, 50), text='NORMAL MODE', manager=manager)
        self.story_mode_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            self.screen_width // 2 - 100, self.screen_height // 2 * 1.3, 200, 50), text='STORY MODE', manager=manager)

        # 이벤트 처리 함수
    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.normal_mode_button:
                self.next_screen = LobbyScreen
                self.is_running = False
            elif event.ui_element == self.story_mode_button:
                self.next_screen = MapScreen
                self.is_running = False


         # run 함수
    def run(self, events: list[Event]) -> bool:
        
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text, self.text_rect)

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running