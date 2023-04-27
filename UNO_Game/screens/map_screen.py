import pygame
import pygame.freetype
import pygame_gui
import json
from pygame.event import Event
from pygame.surface import Surface
from pygame_gui.elements import UITextEntryLine, UIButton

from client.networking import Networking
from screens.abc_screen import Screen


class MapScreen(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)


class MapScreen(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        # json 파일 로드
        with open('display_config.json', 'r') as f:
            config_data = json.load(f)
        with open('keys.json', 'r') as f:
            keyboard_data = json.load(f)

        self.screen_width = config_data['resolution']['width']
        self.screen_height = config_data['resolution']['height']
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.keyboard_right = keyboard_data["keyboard"]["right"]
        self.keyboard_left = keyboard_data["keyboard"]["left"]

        self.screen_width = config_data['resolution']['width']
        self.screen_height = config_data['resolution']['height']
        self.width = config_data['resolution']['width']
        self.height = config_data['resolution']['height']
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE
        self.next_screen = None

        self.manager = manager

        # 이미지 로드
        self.image1 = pygame.image.load("assets/images/example1_inactive.png")
        self.image2 = pygame.image.load("assets/images/example1_active.png")
        self.image3 = pygame.image.load("assets/images/example2_inactive.png")
        self.image4 = pygame.image.load("assets/images/example2_active.png")
        self.image5 = pygame.image.load("assets/images/example3_inactive.png")
        self.image6 = pygame.image.load("assets/images/example3_active.png")
        self.image7 = pygame.image.load("assets/images/example4_inactive.png")
        self.image8 = pygame.image.load("assets/images/example4_active.png")
        self.image9 = pygame.image.load("assets/images/example5-1.png")
        self.image10 = pygame.image.load("assets/images/example5-2.png")
        self.image11 = pygame.image.load("assets/images/example5-3.png")

        # 이미지 rect 설정
        self.image_rect = self.image1.get_rect()
        self.image_rect.center = (
            self.screen_width // 2 * 0.3, self.screen_height // 2 * 0.5)
        self.image_rect2 = self.image3.get_rect()
        self.image_rect2.center = (
            self.screen_width // 2 * 0.75, self.screen_height // 2 * 1.1)
        self.image_rect3 = self.image5.get_rect()
        self.image_rect3.center = (
            self.screen_width // 2 * 1.15, self.screen_height // 2 * 0.8)
        self.image_rect4 = self.image7.get_rect()
        self.image_rect4.center = (
            self.screen_width // 2 * 1.6, self.screen_height // 2 * 1.3)
        self.image_rect5 = self.image9.get_rect()
        self.image_rect5.center = (
            self.screen_width // 2 * 0.6, self.screen_height // 2 * 0.5)
        self.image_rect6 = self.image10.get_rect()
        self.image_rect6.center = (
            self.screen_width // 2 * 1.05, self.screen_height // 2 * 1.3)
        self.image_rect7 = self.image11.get_rect()
        self.image_rect7.center = (
            self.screen_width // 2 * 1.5, self.screen_height // 2 * 0.8)

        # 이미지 리스트 생성
        self.image_list = [self.image1, self.image3, self.image5, self.image7]
        self.num_images = len(self.image_list)
        self.selected_index = 0

        # 현재 이미지 설정
        self.current_image = self.image1
        self.current_image2 = self.image3
        self.current_image3 = self.image5
        self.current_image4 = self.image7
        self.current_image5 = self.image9
        self.current_image6 = self.image10
        self.current_image7 = self.image11

        # 버튼 생성
        self.button_rect = pygame.Rect(
            (self.screen_width // 2 * 0.8, self.screen_height // 2 * 1.7), (self.screen_width // 5, self.screen_height // 15))
        self.home_button = UIButton(
            relative_rect=self.button_rect, text='HOME', manager=manager)

    # 팝업창 함수
    def create_popup(self, manager):
        popup_window = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(
                (self.screen_width//2 * 0.5, self.screen_height//2 * 0.6), (450, 250)),
            manager=manager,
            window_title='PlAY GAME',
            action_long_desc='Are you sure to play Stage 1?',
            action_short_name='OK',
            blocking=True)
        return popup_window

    def create_popup2(self, manager):
        popup_window = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(
                (self.screen_width//2 * 0.5, self.screen_height//2 * 0.6), (450, 250)),
            manager=manager,
            window_title='PlAY GAME',
            action_long_desc='Are you sure to play Stage 2?',
            action_short_name='OK',
            blocking=True)
        return popup_window

    def create_popup3(self, manager):
        popup_window = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(
                (self.screen_width//2 * 0.5, self.screen_height//2 * 0.6), (450, 250)),
            manager=manager,
            window_title='PlAY GAME',
            action_long_desc='Are you sure to play Stage 3?',
            action_short_name='OK',
            blocking=True)
        return popup_window

    def create_popup4(self, manager):
        popup_window = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(
                (self.screen_width//2 * 0.5, self.screen_height//2 * 0.6), (450, 250)),
            manager=manager,
            window_title='PlAY GAME',
            action_long_desc='Are you sure to play Stage 4?',
            action_short_name='OK',
            blocking=True)
        return popup_window

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.image_rect.collidepoint(event.pos):
                if self.current_image == self.image1:
                    self.current_image = self.image2
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                else:
                    self.current_image = self.image1
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
            elif self.image_rect2.collidepoint(event.pos):
                if self.current_image2 == self.image3:
                    self.current_image2 = self.image4
                    self.current_image = self.image1
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                else:
                    self.current_image2 = self.image3
                    self.current_image = self.image1
                    self.urrent_image3 = self.image5
                    self.current_image4 = self.image7
            elif self.image_rect3.collidepoint(event.pos):
                if self.current_image3 == self.image5:
                    self.current_image3 = self.image6
                    self.current_image2 = self.image3
                    self.current_image = self.image1
                    self.current_image4 = self.image7
                else:
                    self.current_image3 = self.image5
                    self.current_image2 = self.image3
                    self.current_image = self.image1
                    self.current_image4 = self.image7
            elif self.image_rect4.collidepoint(event.pos):
                if self.current_image4 == self.image7:
                    self.current_image4 = self.image8
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image = self.image1
                else:
                    self.current_image4 = self.image7
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image = self.image1
        # 이미지 로드
        self.image1 = pygame.image.load("assets/images/example1_inactive.png")
        self.image2 = pygame.image.load("assets/images/example1_active.png")
        self.image3 = pygame.image.load("assets/images/example2_inactive.png")
        self.image4 = pygame.image.load("assets/images/example2_active.png")
        self.image5 = pygame.image.load("assets/images/example3_inactive.png")
        self.image6 = pygame.image.load("assets/images/example3_active.png")
        self.image7 = pygame.image.load("assets/images/example4_inactive.png")
        self.image8 = pygame.image.load("assets/images/example4_active.png")
        self.image9 = pygame.image.load("assets/images/example5-1.png")
        self.image10 = pygame.image.load("assets/images/example5-2.png")
        self.image11 = pygame.image.load("assets/images/example5-3.png")

        # 이미지 rect 설정
        self.image_rect = self.image1.get_rect()
        self.image_rect.center = (
            self.screen_width // 2 * 0.3, self.screen_height // 2 * 0.5)
        self.image_rect2 = self.image3.get_rect()
        self.image_rect2.center = (
            self.screen_width // 2 * 0.75, self.screen_height // 2 * 1.1)
        self.image_rect3 = self.image5.get_rect()
        self.image_rect3.center = (
            self.screen_width // 2 * 1.15, self.screen_height // 2 * 0.8)
        self.image_rect4 = self.image7.get_rect()
        self.image_rect4.center = (
            self.screen_width // 2 * 1.6, self.screen_height // 2 * 1.3)
        self.image_rect5 = self.image9.get_rect()
        self.image_rect5.center = (
            self.screen_width // 2 * 0.6, self.screen_height // 2 * 0.5)
        self.image_rect6 = self.image10.get_rect()
        self.image_rect6.center = (
            self.screen_width // 2 * 1.05, self.screen_height // 2 * 1.3)
        self.image_rect7 = self.image11.get_rect()
        self.image_rect7.center = (
            self.screen_width // 2 * 1.5, self.screen_height // 2 * 0.8)

        # 이미지 리스트 생성
        self.image_list = [self.image1, self.image3, self.image5, self.image7]
        self.num_images = len(self.image_list)
        self.selected_index = 0

        # 현재 이미지 설정
        self.current_image = self.image1
        self.current_image2 = self.image3
        self.current_image3 = self.image5
        self.current_image4 = self.image7
        self.current_image5 = self.image9
        self.current_image6 = self.image10
        self.current_image7 = self.image11

        # 버튼 생성
        self.button_rect = pygame.Rect(
            (self.screen_width // 2 * 0.8, self.screen_height // 2 * 1.7), (self.screen_width // 5, self.screen_height // 15))
        self.home_button = UIButton(
            relative_rect=self.button_rect, text='HOME', manager=self.manager)

        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render(
            "The computer player will receive a 50% higher chance of receiving a skill card.", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.width // 2, self.height // 2 * 0.1)

        self.text2 = self.font.render(
            "Battle with 3 computer players", True, (0, 0, 0))
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = (self.width // 2, self.height // 2 * 0.1)

        self.text3 = self.font.render(
            "Battle with 2 computer players", True, (0, 0, 0))
        self.text_rect3 = self.text3.get_rect()
        self.text_rect3.center = (self.width // 2, self.height // 2 * 0.1)

        self.text4 = self.font.render(
            "Battle with 4 computer players", True, (0, 0, 0))
        self.text_rect4 = self.text4.get_rect()
        self.text_rect4.center = (self.width // 2, self.height // 2 * 0.1)

        self.show_text1 = False
        self.show_text2 = False
        self.show_text3 = False
        self.show_text4 = False

    # 팝업창 함수
    def create_popup(self, manager):
        popup_window = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(
                (self.screen_width//2 * 0.5, self.screen_height//2 * 0.6), (450, 250)),
            manager=manager,
            window_title='PLAY GAME',
            action_long_desc='Are you sure to play Stage 1?',
            action_short_name='OK',
            blocking=True)
        return popup_window

    def create_popup2(self, manager):
        popup_window = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(
                (self.screen_width//2 * 0.5, self.screen_height//2 * 0.6), (450, 250)),
            manager=manager,
            window_title='PLAY GAME',
            action_long_desc='Are you sure to play Stage 2?',
            action_short_name='OK',
            blocking=True)
        return popup_window

    def create_popup3(self, manager):
        popup_window = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(
                (self.screen_width//2 * 0.5, self.screen_height//2 * 0.6), (450, 250)),
            manager=manager,
            window_title='PLAY GAME',
            action_long_desc='Are you sure to play Stage 3?',
            action_short_name='OK',
            blocking=True)
        return popup_window

    def create_popup4(self, manager):
        popup_window = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(
                (self.screen_width//2 * 0.5, self.screen_height//2 * 0.6), (450, 250)),
            manager=manager,
            window_title='PLAY GAME',
            action_long_desc='Are you sure to play Stage 4?',
            action_short_name='OK',
            blocking=True)
        return popup_window

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.image_rect.collidepoint(event.pos):
                if self.current_image == self.image1:
                    self.current_image = self.image2
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                    self.show_text1 = True
                else:
                    self.current_image = self.image1
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
            elif self.image_rect2.collidepoint(event.pos):
                if self.current_image2 == self.image3:
                    self.current_image2 = self.image4
                    self.current_image = self.image1
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                    self.show_text2 = True
                else:
                    self.current_image2 = self.image3
                    self.current_image = self.image1
                    self.urrent_image3 = self.image5
                    self.current_image4 = self.image7
            elif self.image_rect3.collidepoint(event.pos):
                if self.current_image3 == self.image5:
                    self.current_image3 = self.image6
                    self.current_image2 = self.image3
                    self.current_image = self.image1
                    self.current_image4 = self.image7
                    self.show_text3 = True
                else:
                    self.current_image3 = self.image5
                    self.current_image2 = self.image3
                    self.current_image = self.image1
                    self.current_image4 = self.image7
            elif self.image_rect4.collidepoint(event.pos):
                if self.current_image4 == self.image7:
                    self.current_image4 = self.image8
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image = self.image1
                    self.show_text4 = True
                else:
                    self.current_image4 = self.image7
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image = self.image1
        elif event.type == pygame.MOUSEBUTTONUP:
            self.show_text1 = False
            self.show_text2 = False
            self.show_text3 = False
            self.show_text4 = False
        elif event.type == pygame.KEYDOWN:
            if event.key == self.keyboard_left:
                self.selected_index = (
                    self.selected_index - 1) % self.num_images
                if self.selected_index == 0:
                    self.current_image4 = self.image8
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image = self.image1
                elif self.selected_index == 1:
                    self.current_image = self.image2
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                elif self.selected_index == 2:
                    self.current_image2 = self.image4
                    self.current_image = self.image1
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                elif self.selected_index == 3:
                    self.current_image3 = self.image6
                    self.current_image2 = self.image3
                    self.current_image = self.image1
                    self.current_image4 = self.image7

            elif event.key == self.keyboard_right:
                self.selected_index = (
                    self.selected_index + 1) % self.num_images
                if self.selected_index == 0:
                    self.current_image4 = self.image8
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image = self.image1
                elif self.selected_index == 1:
                    self.current_image = self.image2
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                elif self.selected_index == 2:
                    self.current_image2 = self.image4
                    self.current_image = self.image1
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                elif self.selected_index == 3:
                    self.current_image3 = self.image6
                    self.current_image2 = self.image3
                    self.current_image = self.image1
                    self.current_image4 = self.image7

            elif event.key == pygame.K_RETURN:
                if self.selected_index == 0:
                    self.current_image4 = self.image8
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image = self.image1
                    self.show_text4 = True
                elif self.selected_index == 1:
                    self.current_image = self.image2
                    self.current_image2 = self.image3
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                    self.show_text1 = True
                elif self.selected_index == 2:
                    self.current_image2 = self.image4
                    self.current_image = self.image1
                    self.current_image3 = self.image5
                    self.current_image4 = self.image7
                    self.show_text2 = True
                elif self.selected_index == 3:
                    self.current_image3 = self.image6
                    self.current_image2 = self.image3
                    self.current_image = self.image1
                    self.current_image4 = self.image7
                    self.show_text3 = True

        if self.current_image == self.image2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.popup_window = self.create_popup(self.manager)

        if self.current_image2 == self.image4:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.popup_window = self.create_popup2(self.manager)

        if self.current_image3 == self.image6:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.popup_window = self.create_popup3(self.manager)

        if self.current_image4 == self.image8:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.popup_window = self.create_popup4(self.manager)

        if event.type == pygame.USEREVENT:
            if self.popup_window and event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                if event.ui_object == self.popup_window:
                    self.popup_window.kill()
                    self.popup_window = None

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.home_button:
                from screens.start_screen import StartScreen
                self.next_screen = StartScreen
                self.is_running = False

# run 함수
    def run(self, events: list[Event]) -> bool:

        self.screen.blit(self.background, (0, 0))
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.current_image, self.image_rect)
        self.screen.blit(self.current_image2, self.image_rect2)
        self.screen.blit(self.current_image3, self.image_rect3)
        self.screen.blit(self.current_image4, self.image_rect4)
        self.screen.blit(self.current_image5, self.image_rect5)
        self.screen.blit(self.current_image6, self.image_rect6)
        self.screen.blit(self.current_image7, self.image_rect7)

        if self.show_text1:
            self.screen.blit(self.text, self.text_rect)
        if self.show_text2:
            self.screen.blit(self.text2, self.text_rect2)
        if self.show_text3:
            self.screen.blit(self.text3, self.text_rect3)
        if self.show_text4:
            self.screen.blit(self.text4, self.text_rect4)

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running


# run 함수

    def run(self, events: list[Event]) -> bool:

        self.screen.blit(self.background, (0, 0))
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.current_image, self.image_rect)
        self.screen.blit(self.current_image2, self.image_rect2)
        self.screen.blit(self.current_image3, self.image_rect3)
        self.screen.blit(self.current_image4, self.image_rect4)
        self.screen.blit(self.current_image5, self.image_rect5)
        self.screen.blit(self.current_image6, self.image_rect6)
        self.screen.blit(self.current_image7, self.image_rect7)

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running
