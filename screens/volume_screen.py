import pygame
import pygame.freetype
import pygame_gui
import json
from pygame.surface import Surface
from pygame.event import Event
from pygame_gui.elements.ui_button import UIButton

from utility import resolution
from client.networking import Networking
from screens.abc_screen import Screen


class VolumeScreen(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        with open('display_config.json', 'r') as f:
            config_data = json.load(f)

        with open('volume_setting.json', 'r') as f:
            data = json.load(f)
            self.slider1_start_value = data["slider1_value"]
            self.slider2_start_value = data["slider2_value"]
            self.slider3_start_value = data["slider3_value"]

        self.screen_width = config_data['resolution']['width']
        self.screen_height = config_data['resolution']['height']
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE

        self.font = pygame.font.SysFont(None, 100)
        self.uni_font = pygame.font.SysFont(None, 30)

        # "Volume" 텍스트 생성
        self.text = self.font.render("VOLUME", True, (255, 255, 255))
        self.text1 = self.uni_font.render(
            "Static Sound", True, (255, 255, 255))
        self.text2 = self.uni_font.render("Background", True, (255, 255, 255))
        self.text3 = self.uni_font.render(
            "Sound Effect", True, (255, 255, 255))

        # 텍스트의 중심 좌표 계산
        self.text_rect = self.text.get_rect(
            center=(self.screen_width//2, self.screen_height//2 * 0.5))
        self.text1_rect = self.text1.get_rect(
            center=(self.screen_width // 2 * 0.5, self.screen_height // 2))
        self.text2_rect = self.text2.get_rect(
            center=(self.screen_width // 2 * 0.5, self.screen_height // 2 * 1.3))
        self.text3_rect = self.text3.get_rect(
            center=(self.screen_width // 2 * 0.5, self.screen_height // 2 * 1.6))

        self.slider1 = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(
                (self.screen_width // 2, self.screen_height // 2 * 0.9), (self.screen_width // 4, self.screen_height // 12)),
            start_value=self.slider1_start_value,
            value_range=(0.0, 100.0, 1.0),
            manager=manager
        )

        self.slider2 = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(
                (self.screen_width // 2, self.screen_height // 2 * 1.2), (self.screen_width // 4, self.screen_height // 12)),
            start_value=self.slider2_start_value,
            value_range=(0.0, 100.0, 1.0),
            manager=manager
        )

        self.slider3 = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(
                (self.screen_width // 2, self.screen_height // 2 * 1.5), (self.screen_width // 4, self.screen_height // 12)),
            start_value=self.slider3_start_value,
            value_range=(0.0, 100.0, 1.0),
            manager=manager
        )

        # 나가기버튼 생성
        self.button_rect = pygame.Rect(
            (self.screen_width // 2 * 0.75, self.screen_height // 2 * 1.8), (self.screen_width // 5, self.screen_height // 15))
        self.exit_button = UIButton(
            relative_rect=self.button_rect, text='Exit', manager=manager)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.exit_button:
                # 순환 참조때문에 import 조금 늦게~ㅎ
                from screens.setting_screen import SettingScreen
                self.next_screen = SettingScreen
                self.is_running = False

         # run 함수
    def run(self, events: list[Event]) -> bool:

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text1, self.text1_rect)
        self.screen.blit(self.text2, self.text2_rect)
        self.screen.blit(self.text3, self.text3_rect)

        for event in events:
            self.handle_event(event)
            self.data = {"slider1_value": self.slider1.get_current_value(
            ), "slider2_value": self.slider2.get_current_value(), "slider3_value": self.slider3.get_current_value()}
            with open("volume_setting.json", "w") as f:
                json.dump(self.data, f)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running
