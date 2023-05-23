import json
import sys
import pygame
import pygame.freetype
import pygame_gui
from pygame.event import Event
from pygame.surface import Surface
from pygame_gui import UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton

from client.networking import Networking
from screens.abc_screen import Screen
# from screens.end_screen import EndScreen
from utility import resolution


class CharacterScreen(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        self.screen_width, self.screen_height = resolution()
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE
        # self.next_screen = MainScreen
        self.next_screen = None

        with open('player_num.json', 'r') as f:
            player_data = json.load(f)

        if player_data:
            player_info = player_data[0]  # 첫 번째 사전만 읽어옴
            self.computer_number = player_info.get("computer_number", 0)
            self.user_name = player_info.get("user_name", "")
        else:
            self.computer_number = 0
            self.user_name = ""

        print("컴퓨터 수:" + str(self.computer_number) + "유저 이름:" + self.user_name)

        self.text_title_content = "Character"
        self.font_title = pygame.font.Font(None, 100)
        self.text_title = self.font_title.render(
            self.text_title_content, True, (255, 255, 255))
        self.text_character_rect = self.text_title.get_rect(
            center=(self.screen_width // 2, self.screen_height // 2 * 0.3))

        self.image_path = ["assets/images/character0.png", "assets/images/character1.png",
                           "assets/images/character2.png", "assets/images/character3.png", "assets/images/character4.png"]
        self.images = []
        self.image_rects = []

        for path in self.image_path:
            self.image = pygame.image.load(path)
            self.images.append(self.image)
            self.image_rect = self.image.get_rect()
            self.image_rects.append(self.image_rect)

        # 이미지 위치 설정
        self.image_count = len(self.images)
        self.image_width = self.image_rects[0].width
        self.image_height = self.image_rects[0].height
        self.spacing = 20  # 이미지 사이의 간격
        self.total_width = (self.image_width + self.spacing) * \
            self.image_count - self.spacing  # 이미지와 간격을 포함한 총 너비
        self.start_x = self.screen_width // 2 - \
            self.total_width // 2  # 이미지를 가운데에 정렬하기 위한 시작 위치

        for i in range(self.image_count):
            self.image_rects[i].x = self.start_x + \
                (self.image_width + self.spacing) * i
            self.image_rects[i].y = self.screen_height // 2 - \
                self.image_height // 2

        self.selected_characters = set()

        self.button_rect = pygame.Rect(
            (self.screen_width // 2 * 0.8, self.screen_height // 2 * 1.7), (self.screen_width // 5, self.screen_height // 15))
        self.home_button = UIButton(
            relative_rect=self.button_rect, text='HOME', manager=manager)

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, image_rect in enumerate(self.image_rects):
                if image_rect.collidepoint(mouse_pos):
                    if i not in self.selected_characters:
                        self.selected_characters.add(i)
                        print("캐릭터", i, "을(를) 선택했습니다.")
                    else:
                        self.selected_characters.remove(i)
                        print("캐릭터", i, "의 선택을 취소했습니다.")
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.home_button:
                    from screens.start_screen import StartScreen
                    self.next_screen = StartScreen
                    self.is_running = False

    def run(self, events: list[Event]) -> bool:
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text_title, self.text_character_rect)

        for i in range(self.image_count):
            if i in self.selected_characters:
                pygame.draw.rect(self.screen, (0, 255, 0),
                                 self.image_rects[i], 3)
            self.screen.blit(self.images[i], self.image_rects[i])
        for event in events:
            self.handle_events(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running
