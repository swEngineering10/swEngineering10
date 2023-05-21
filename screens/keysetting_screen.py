import pygame
import pygame.freetype
import pygame_gui
import json
import sys
from pygame.event import Event
from pygame.surface import Surface
from pygame_gui.elements import UITextEntryLine, UIButton

from utility import resolution
from client.networking import Networking
from screens.abc_screen import Screen


class KeyScreen(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        with open('display_config.json', 'r') as f:
            config_data = json.load(f)

        self.screen_width = config_data['resolution']['width']
        self.screen_height = config_data['resolution']['height']
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE
        self.next_screen = None

        self.manager = manager

        self.font = pygame.font.SysFont(None, 100)
        self.text = self.font.render("KEY SETTING", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(
            center=(self.screen_width // 2, self.screen_height // 2 * 0.4))

        self.DEFAULT_KEYS = {
            "UP": "up",
            "DOWN": "down",
            "LEFT": "left",
            "RIGHT": "right"
        }

        self.KEYS_FILE_PATH = "keys.json"

        try:
            with open(self.KEYS_FILE_PATH, "r") as f:
                self.keys = json.load(f)
        except:
            self.keys = self.DEFAULT_KEYS

    # screen = pygame.display.set_mode((screen_width, screen_height))

    # manager = pygame_gui.UIManager(screen.get_size())

        self.up_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.screen_width // 2 * 0.75, self.screen_height // 2 * 0.7), (200, 50)),
            text='UP Key: ' + pygame.key.name(self.keys["1073741906"]),
            manager=manager
        )

        self.down_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.screen_width // 2 * 0.75, self.screen_height // 2 * 0.7 * 1.4), (200, 50)),
            text='DOWN Key: ' + pygame.key.name(self.keys["1073741905"]),
            manager=manager
        )

        self.left_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.screen_width // 2 * 0.75, self.screen_height // 2 * 0.7 * 1.8), (200, 50)),
            text='LEFT Key: ' + pygame.key.name(self.keys["1073741904"]),
            manager=manager
        )

        self.right_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.screen_width // 2 * 0.75, self.screen_height // 2 * 0.7 * 2.2), (200, 50)),
            text='RIGHT Key: ' + pygame.key.name(self.keys["1073741903"]),
            manager=manager
        )

        self.button_rect = pygame.Rect(
            (self.screen_width // 2 * 0.8, self.screen_height // 2 * 0.7 * 2.5), (self.screen_width // 5, self.screen_height // 15))
        self.exit_button = UIButton(
            relative_rect=self.button_rect, text='Exit', manager=manager)

    def change_key(self, key):
        self.new_key = None
        while self.new_key is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.new_key = event.key

        self.keys[key] = self.new_key

        print(pygame.key.name(self.new_key))
        '''
    clock = pygame.time.Clock()
    while running:
        time_delta = clock.tick(60) / 1000.0
        '''

    def handle_event(self, event):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.up_button:
                        self.change_key(pygame.K_UP)
                        self.up_button.set_text(
                            'UP Key: ' + pygame.key.name(self.keys[pygame.K_UP]))
                    elif event.ui_element == self.down_button:
                        self.change_key(pygame.K_DOWN)
                        self.down_button.set_text(
                            'DOWN Key: ' + pygame.key.name(self.keys[pygame.K_DOWN]))
                    elif event.ui_element == self.left_button:
                        self.change_key(pygame.K_LEFT)
                        self.left_button.set_text(
                            'LEFT Key: ' + pygame.key.name(self.keys[pygame.K_LEFT]))
                    elif event.ui_element == self.right_button:
                        self.change_key(pygame.K_RIGHT)
                        self.right_button.set_text(
                            'RIGHT Key: ' + pygame.key.name(self.keys[pygame.K_RIGHT]))
                    elif event.ui_element == self.exit_button:
                        from screens.setting_screen import SettingScreen
                        self.next_screen = SettingScreen
                        self.is_running = False

            self.manager.process_events(event)

    def run(self, events: list[Event]) -> bool:
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text, self.text_rect)

        # self.manager.update(self.time_delta)

        self.manager.draw_ui(self.screen)

        pygame.display.flip()

        with open("keys.json", "w") as f:
            json.dump(self.keys, f)

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running

    # pygame.quit()


# run_key_changer()
