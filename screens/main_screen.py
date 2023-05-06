import pygame
import pygame.freetype
import pygame_gui
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pygame.surface import Surface
from pygame.event import Event



from game_logic import init
from game_logic import split_cards
from utility import resolution

from utility import BackGround
from game_class import GameInit
from utility import CardLoad
from client.networking import Networking
from screens.abc_screen import Screen

class MainScreen(Screen):
    def __init__(self, surface: Surface, manager: pygame_gui.UIManager, networking: Networking):
        super().__init__(surface, manager, networking)

        self.screen_width, self.screen_height = resolution()
        WINDOW_SIZE = (self.screen_width, self.screen_height)

        self.background = pygame.Surface(WINDOW_SIZE)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.screen_width, self.screen_height = WINDOW_SIZE

        # 배경화면 객체 생성
        self.background = BackGround()

        # UNO 버튼 생성
        self.UNO_button_width = 100
        self.UNO_button_height = 50
        self.start_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((420, 280), (self.UNO_button_width, self.UNO_button_height)),
                text=str("UNO"),
                manager=manager
            )

        # 카드 덱 (미오픈) 이미지 로드
        # 주의점 : 만약에 카드를 다 썼다면 지우는게 맞는듯!!
        self.card_back = pygame.image.load("C:/Python/3_1_project/10weeks_2/UNO_Game/assets/images/cards/card_back.png")
        
        # 게임 객체 생성
        self.game_init = GameInit()
        self.game_init.numPlayers = 2  # 플레이어의 수 2라고 가정 (나중에 로비에서 값 받아야 함!!)

        # 게임 초기화 (카드 생성, 셔플, 맨 위 카드 꺼내기)
        init(self.game_init)

        # currentCard 이미지 로드 객체 생성
        self.currentCardImage = CardLoad(self.game_init.currentCard)
        
        # 유저 보유 카드 리스트 모두 CardLoad 객체 생성 후 이미지 로드
        split_cards(self.game_init)
        print(self.game_init.playerList[0]) # 내 카드 출력 (확인용)

        self.my_card_list = []
        for i in range(len(self.game_init.playerList[0])) :
            self.my_card_list.append(CardLoad(self.game_init.playerList[0][i]))
            self.my_card_list[i].card_pop_image(self.my_card_list)

        # computer 카드 나눠주기 (뒷면 이미지 로드)


    # 이벤트 처리 함수
    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            pass


    # run 함수
    def run(self, events: list[Event]) -> bool:
        
        # 배경화면
        self.background.background_draw(self.screen)

        # 카드 덱
        self.screen.blit(self.card_back, (60, 60))

        # currentCard 이미지
        self.currentCardImage.current_card_draw(self.screen)

        # 처음 카드 7장
        for i in range(len(self.my_card_list)):
            self.my_card_list[i].image_animation(self.screen)

        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running