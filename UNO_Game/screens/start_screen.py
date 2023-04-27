import pygame
import pygame.freetype
import pygame_gui
import json
from pygame.event import Event
from pygame.surface import Surface
from pygame_gui.elements import UITextEntryLine, UIButton

from client.networking import Networking
from screens.abc_screen import Screen
from screens.lobby_screen import LobbyScreen
from screens.setting_screen import SettingScreen
from screens.mode_screen import ModeScreen


class StartScreen(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        # json 파일 로드
        with open('display_config.json', 'r') as f:
            config_data = json.load(f)

        with open('keys.json', 'r') as f:
            keyboard_data = json.load(f)

        self.key_up = keyboard_data["keyboard"]["up"]
        self.key_down = keyboard_data["keyboard"]["down"]

        self.screen_width = config_data['resolution']['width']
        self.screen_height = config_data['resolution']['height']
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE
        self.next_screen = ModeScreen

        # UNO 텍스트 생성
        self.font = pygame.font.SysFont(None, 100)
        self.text = self.font.render("UNO", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(
            center=(self.screen_width//2, self.screen_height*0.3))

        # 버튼 생성
        self.button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            self.screen_width // 2 - 100, self.screen_height // 2, 200, 50), text='SINGLE PLAY', manager=manager)
        self.button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            self.screen_width // 2 - 100, self.screen_height // 2 * 1.3, 200, 50), text='SETTING', manager=manager)
        self.button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            self.screen_width // 2 - 100, self.screen_height // 2 * 1.6, 200, 50), text='EXIT', manager=manager)

        buttons = [self.button1, self.button2, self.button3]

        self.buttons = buttons
        self.selected_button_index = 0
        self.buttons[self.selected_button_index]._set_active()

    def play_mode_function(self):
        self.next_screen = ModeScreen
        self.is_running = False

    def setting_mode_function(self):
        self.next_screen = SettingScreen
        self.is_running = False

    def exit_mode_function(self):
        print('Exit!')
        pygame.quit()
        quit()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_up:
                self.selected_button_index = (
                    self.selected_button_index - 1) % len(self.buttons)
                self.buttons[self.selected_button_index]._set_active()
                self.buttons[(self.selected_button_index + 1) %
                             len(self.buttons)].unselect()
                self.buttons[(self.selected_button_index + 1) %
                             len(self.buttons)].enable()
            elif event.key == self.key_down:
                self.selected_button_index = (
                    self.selected_button_index + 1) % len(self.buttons)
                self.buttons[(self.selected_button_index) %
                             len(self.buttons)]._set_active()
                self.buttons[(self.selected_button_index - 1) %
                             len(self.buttons)].unselect()
                self.buttons[(self.selected_button_index - 1) %
                             len(self.buttons)].enable()
            elif event.key == pygame.K_RETURN:
                clicked_button = self.buttons[self.selected_button_index]
                if clicked_button == self.button1:
                    self.play_mode_function()
                elif clicked_button == self.button2:
                    self.setting_mode_function()
                else:
                    self.exit_mode_function()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for i, button in enumerate(self.buttons):
                if event.ui_element == button:
                    if button == self.button1:
                        self.play_mode_function()
                    elif button == self.button2:
                        self.setting_mode_function()
                    else:
                        self.exit_mode_function()

     # run 함수

    def run(self, events: list[Event]) -> bool:

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text, self.text_rect)

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running
