import pygame
import pygame.freetype
import pygame_gui
import sys
import json
from pygame.surface import Surface
from pygame.event import Event
from pygame_gui.elements.ui_button import UIButton

from utility import resolution
from client.networking import Networking
from screens.abc_screen import Screen


class GameScreen(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        self.screen_width, self.screen_height = resolution()
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE
        self.next_screen = None

        # 딕셔너리 생성
        self.data = {"resolution": {
            "width": self.screen_width, "height": self.screen_height}}

        self.button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (350, 275), (100, 50)), text='Win', manager=manager)

    def handle_event(self, event):
        self.win_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.button:
                        self.win_pressed = True

        if self.win_pressed:
            with open('win.json', 'w') as f:
                json.dump(True, f)
            from screens.map_screen import MapScreen
            self.next_screen = MapScreen
            self.is_running = False

            self.manager.process_events(event)

    def run(self, events: list[Event]) -> bool:
        self.screen.fill((255, 255, 255))
        self.manager.draw_ui(self.screen)

        pygame.display.flip()

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running


# 함수 호출하여 실행
'''
result = show_win_button()
print(result)
'''
