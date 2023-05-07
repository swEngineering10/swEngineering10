import pygame
import pygame.freetype
import pygame_gui
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pygame.surface import Surface
from pygame.event import Event

from game_logic import init
from game_logic import split_cards
from game_logic import play_game
from game_logic import game_end
from AIplayer import ai_play_game
from utility import resolution
from utility import card_click

from utility import PlayerState
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
        self.card_back = CardLoad(("card", "back"))
        
        # 게임 객체 생성
        self.game_init = GameInit()
        self.game_init.numPlayers = 2  # 플레이어의 수 2라고 가정 (나중에 로비에서 값 받아야 함!!)

        # 게임 초기화 (카드 생성, 셔플, 맨 위 카드 꺼내기)
        init(self.game_init)

        # currentCard 이미지 로드 객체 생성
        self.currentCardImage = CardLoad(self.game_init.currentCard)
        
        # 유저 보유 카드 리스트 모두 CardLoad 객체 생성 후 이미지 로드
        split_cards(self.game_init)

        self.my_card_list = []
        for i in range(len(self.game_init.playerList[0])) :
            self.my_card_list.append(CardLoad(self.game_init.playerList[0][i]))
            self.my_card_list[i].card_pop_image(self.my_card_list)

        # computer player 이미지 객체 생성
        self.player1 = PlayerState(1)

        # 게임 시작
        # self.game()

    def game(self) :
        if self.game_init.myTurn == self.game_init.playerTurn :
            play_game(self.game_init, self.game_init.playerList[self.game_init.playerTurn])
        else:
            ai_play_game(self.game_init, self.game_init.playerList[self.game_init.playerTurn])


    # 이벤트 처리 함수
    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            pass

    
    # 이미지 이벤트 처리 함수
    def handle_event_image(self, event, surface):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            card_click(self.my_card_list, self.game_init, self.card_back, mouse_pos, surface)


    # run 함수
    def run(self, events: list[Event]) -> bool:
        
        # 배경화면
        self.background.background_draw(self.screen)

        # 카드 덱
        self.card_back.card_load(self.screen, self.card_back.deck_pos)

        # currentCard 이미지
        self.currentCardImage.card_load(self.screen, self.currentCardImage.current_card_pos)

        # 처음 카드 7장
        for i in range(len(self.my_card_list)):
            self.my_card_list[i].image_animation(self.screen)

        # 컴퓨터 플레이어 카드 로드
        self.player1.player_state_draw(self.screen)

        while self.game_init.running:   # 테스트
            self.game()

        for event in events:
            self.handle_event(event)
            self.handle_event_image(event, self.screen)
        

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running