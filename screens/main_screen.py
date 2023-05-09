import pygame
import pygame.freetype
import pygame_gui
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pygame.surface import Surface
from pygame.event import Event

from game_logic import init
from game_logic import split_cards
from game_logic import play_game
from game_logic import game_end
from AIplayer import ai_play_game
from utility import resolution

from utility import PlayerState
from utility import BackGround
from utility import handle_click_card
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
        
        # 게임 객체 생성
        self.game_init = GameInit()
        self.game_init.numPlayers = 2  # 플레이어의 수 2라고 가정 (나중에 로비에서 값 받아야 함!!)

        # 카드 덱 (미오픈) 이미지 로드
        self.game_init.card_back_image = CardLoad(("card", "back"))

        # 게임 초기화 (카드 생성, 셔플, 맨 위 카드 꺼내기)
        init(self.game_init)

        # currentCard 이미지 로드 객체 생성
        self.game_init.current_card_image = CardLoad(self.game_init.currentCard)
        
        # 유저 보유 카드 리스트 모두 CardLoad 객체 생성 후 이미지 로드
        split_cards(self.game_init)

        for i in range(len(self.game_init.playerList[self.game_init.myTurn])) :
            self.game_init.my_card_list.append(CardLoad(self.game_init.playerList[self.game_init.myTurn][i]))
            self.game_init.my_card_list[i].card_pop_image(self.game_init.my_card_list)

        # computer player 이미지 객체 생성
        self.player1 = PlayerState(1)
        self.game_init.player_deck_image.append(self.player1) # 0번째인 것 고쳐야 함

    
    # 카드 덱
    def deck_image_load(self):
        self.game_init.card_back_image.card_load(self.screen, self.game_init.card_back_image.deck_pos)

    def current_card_load(self):
        self.game_init.current_card_image.card_load(self.screen, self.game_init.card_back_image.current_card_pos)

    # currendtCard 애니메이션
    def current_card_ani(self):
        self.game_init.current_card_image.animation_control(self.screen)

    # 유저 플레이어 카드 로드
    def user_card_load(self):
        for i in range(len(self.game_init.my_card_list)):
            self.game_init.my_card_list[i].animation_control(self.screen)
    
    # 컴퓨터 플레이어 카드 로드
    def player_card_load(self):
        for i in range(len(self.game_init.player_deck_image)) :
            self.game_init.player_deck_image[i].player_state_draw(self.screen)


    # 이벤트 처리 함수
    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            pass


    # run 함수
    def run(self, events: list[Event]) -> bool:

        # 배경화면
        self.background.background_draw(self.screen)

        # 기타 이미지 로드
        self.deck_image_load()
        self.user_card_load()
        self.player_card_load()
        self.current_card_load()


        for event in events:
            # 이벤트 처리
            handle_click_card(event, self.game_init, self.screen)

        # 게임 실행
        if self.game_init.myTurn == self.game_init.playerTurn :
            play_game(self.game_init, self.game_init.playerList[self.game_init.playerTurn])
        else:
            ai_play_game(self.game_init, self.game_init.playerList[self.game_init.playerTurn])



        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running