import pygame
import pygame.freetype
import pygame_gui
import json
from pygame.surface import Surface
from pygame.event import Event
from pygame_gui.elements.ui_button import UIButton

from client.networking import Networking
from screens.abc_screen import Screen
from screens.volume_screen import VolumeScreen

class SettingScreen(Screen):
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
        self.next_screen = VolumeScreen

        # 딕셔너리 생성
        self.data = {"resolution": {"width": self.screen_width, "height": self.screen_height}}

        # 폰트 설정
        self.font = pygame.font.SysFont(None, 100)
        self.uni_font = pygame.font.SysFont(None, 30)
        
        # 텍스트 생성
        self.text_setting = self.font.render("SETTING", True, (255, 255, 255))
        self.text_resolution = self.uni_font.render("Resolution", True, (255, 255, 255))
        self.text_colorchange = self.uni_font.render("Color Change", True, (255, 255, 255))
        self.text_keysetting = self.uni_font.render("Keyboard Setting", True, (255, 255, 255))
        
        # 텍스트의 높이와 너비 구하기
        self.text_setting_rect = self.text_setting.get_rect(center=(self.screen_width//2, self.screen_height//2 * 0.5))
        self.text_resolution_rect = self.text_resolution.get_rect(
            center=(self.screen_width // 2 * 0.5, self.screen_height // 2))
        self.text_colorchange_rect = self.text_colorchange.get_rect(
            center=(self.screen_width // 2 * 0.5, self.screen_height // 2 * 1.3))
        self.text_keysetting_rect = self.text_keysetting.get_rect(
            center=(self.screen_width // 2 * 0.5, self.screen_height // 2 * 1.6))  

        # 화면 해상도 드롭다운 메뉴 생성
        self.resolution_menu = pygame_gui.elements.UIDropDownMenu(
            options_list=["640x480", "800x600", "1024x768"],
            starting_option="800x600",
            relative_rect=pygame.Rect(
                (self.screen_width // 2 * 1.1, self.screen_height // 2 * 0.9), (self.screen_width // 5, self.screen_height // 15)),
            manager=manager
        )

        # 색약모드 변경 드롭다운 메뉴 생성
        self.color_menu = pygame_gui.elements.UIDropDownMenu(
            options_list=['On', 'Off'],
            starting_option='Off',
            relative_rect=pygame.Rect(
                (self.screen_width // 2 * 1.1, self.screen_height // 2 * 1.2), (self.screen_width // 5, self.screen_height // 15)),
            manager=manager)

        # 키보드 설정 변경 드롭다운 메뉴 생성
        self.keyboard_menu = pygame_gui.elements.UIDropDownMenu(
            options_list=["↑, ↓, ←, →", "W, S, A, D"],
            starting_option="↑, ↓, ←, →",
            relative_rect=pygame.Rect(
                (self.screen_width // 2 * 1.1, self.screen_height // 2 * 1.5), (self.screen_width // 5, self.screen_height // 15)),
            manager=manager
        )

        # 리셋버튼 생성
        self.button_rect = pygame.Rect(
            (self.screen_width // 2 * 0.3, self.screen_height // 2 * 1.8), (self.screen_width // 5, self.screen_height // 15))
        self.reset_button = UIButton(
            relative_rect=self.button_rect, text='Reset', manager=manager)

        # 홈버튼 생성
        self.button_rect2 = pygame.Rect(
            (self.screen_width // 2 * 1.4, self.screen_height // 2 * 1.8), (self.screen_width // 5, self.screen_height // 15))
        self.home_button = UIButton(
            relative_rect=self.button_rect2, text='Home', manager=manager)

        # 볼륨버튼 생성
        self.button_rect3 = pygame.Rect(
            (self.screen_width // 2 * 0.85, self.screen_height // 2 * 1.8), (self.screen_width // 5, self.screen_height // 15))
        self.volume_button = UIButton(
            relative_rect=self.button_rect3, text="Volume", manager=manager)

    # 이벤트 처리 함수
    def handle_event(self, event):
        # 드롭다운 메뉴 이벤트
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.resolution_menu:
                self.resolution_str = event.text
                width, height = map(int, self.resolution_str.split("x"))
                self.data["resolution"]["width"] = width
                self.data["resolution"]["height"] = height
                with open('display_config.json', 'w') as f:
                    json.dump(self.data, f)
                self.next_screen = SettingScreen
                self.is_running = False

            elif event.ui_element == self.color_menu:
                # 색약모드 온오프 기능 추가
                pass

            elif event.ui_element == self.keyboard_menu:
                # 키보드 온오프 기능 추가
                pass

        # 버튼 이벤트
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.reset_button:
                self.data["resolution"]["width"] = 800
                self.data["resolution"]["height"] = 600
                with open('display_config.json', 'w') as f:
                    json.dump(self.data, f)
                self.next_screen = SettingScreen
                self.is_running = False

            elif event.ui_element == self.volume_button:
                self.next_screen = VolumeScreen
                self.is_running = False
                pass
            elif event.ui_element == self.home_button:
                # 순환 참조때문에 import 조금 늦게~ㅎ
                from screens.start_screen import StartScreen
                self.next_screen = StartScreen
                self.is_running = False

     # run 함수
    def run(self, events: list[Event]) -> bool:
        
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text_setting, self.text_setting_rect)
        self.screen.blit(self.text_resolution, self.text_resolution_rect)
        self.screen.blit(self.text_colorchange, self.text_colorchange_rect)
        self.screen.blit(self.text_keysetting, self.text_keysetting_rect)

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running