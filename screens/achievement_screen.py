import pygame
import pygame.freetype
import pygame_gui
import json
from pygame.surface import Surface
from pygame.event import Event

from utility import resolution
from client.networking import Networking
from screens.abc_screen import Screen
# from game_logic import load_achievements
from game_class import *


from setting_class import *

ess = Setting()
ob = GameInit()

#업적 로드
# load_achievements(ob)


class Achievement(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        #스크롤 관련 변수
        self.scroll_offset = 0
        self.scroll_speed = 5

        self.screen_width, self.screen_height = resolution()
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE
        # self.next_screen = MainScreen

        # 타이틀 텍스트 내용 및 크기, 위치
        self.text_title_content = "Achievement"
        self.font_title = pygame.font.Font(None, 50)
        self.text_title = self.font_title.render(self.text_title_content, True, (255, 255, 255))
        self.text_title_width, self.text_title_height = self.font_title.size(self.text_title_content)
        self.text_title_x_pos = self.screen_width // 2 - self.text_title_width // 2
        self.text_title_y_pos = self.screen_height * 0.1 + self.scroll_offset


        # 업적 텍스트 내용 및 크기, 위치
        # 텍스트 내용은 아래 achievement_state 함수에서 바뀜
        self.text_achieve_content = 'name'
        self.font_achieve = pygame.font.Font(None, 36)
        self.text_achieve = self.font_achieve.render(self.text_achieve_content, True, (255, 255, 255))
        self.text_achieve_width, self.text_achieve_height = self.font_achieve.size(self.text_achieve_content)
        self.text_achieve_x_pos = self.screen_width // 2 - self.text_achieve_width // 2
        self.text_achieve_y_pos = self.screen_height * 0.4 
        self.screen.blit(self.text_achieve, (self.text_achieve_x_pos, self.text_achieve_y_pos))
        

        # text entry 생성
        self.title_entry_width = 200
        self.title_entry_height = 50
        self.title_entry_x_pos = self.screen_width // 2 - self.title_entry_width // 2
        self.title_entry_y_pos = self.screen_height * 0.2
        self.title_entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.title_entry_x_pos, self.title_entry_y_pos), (self.title_entry_width, self.title_entry_height)),
            manager=manager
        )


        # Game Start 버튼 생성
        self.start_add_player_button_width = 270
        self.start_add_player_button_height = 70
        self.start_add_player_button_x_pos = self.screen_width // 2 - self.start_add_player_button_width // 2
        self.start_add_player_button_y_pos = self.screen_height * 0.8
        self.start_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((self.start_add_player_button_x_pos, self.start_add_player_button_y_pos), (self.start_add_player_button_width, self.start_add_player_button_height)),
                text=str("Game Start"),
                manager=manager
            )
        

    # 업적 상태
    def achievement_state(self):
        # 업적 설명 텍스트 내용 및 크기, 위치
        for index, achievement in enumerate(ob.achievements):
            self.success = "No!!"
            if achievement['count'] != 0:
                self.success = "Success!!!"
            self.text_achieve_content = achievement['name'] + "        " + self.success
            self.font_achieve = pygame.font.Font(None, 36)
            self.text_achieve = self.font_achieve.render(self.text_achieve_content, True, (255, 255, 255))
            self.text_achieve_width, self.text_achieve_height = self.font_achieve.size(self.text_achieve_content)
            self.text_achieve_x_pos = self.screen_width // 2 - self.text_achieve_width // 2
            self.text_achieve_y_pos = self.screen_height * 0.4 + 50 * index + self.scroll_offset
            self.screen.blit(self.text_achieve, (self.text_achieve_x_pos, self.text_achieve_y_pos))

            

    # 이벤트 처리 함수
    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_button:
                if self.username_entry.get_text() == "" :
                    pass
                else :
                    self.user_name = self.username_entry.get_text()
                print(self.user_name)
                # self.next_screen = MainScreen
                # self.is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # 마우스 휠을 위로 스크롤
                self.scroll_offset += self.scroll_speed
            elif event.button == 5:  # 마우스 휠을 아래로 스크롤
                self.scroll_offset -= self.scroll_speed




    # run 함수
    def run(self, events: list[Event]) -> bool:
        
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text_title, (self.text_title_x_pos, self.text_title_y_pos))
        self.achievement_state()

        for event in events:
            self.handle_event(event)



        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running