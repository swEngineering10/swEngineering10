import pygame
import pygame.freetype
import pygame_gui
import json
from pygame.surface import Surface
from pygame.event import Event
from pygame_gui.elements.ui_button import UIButton
from classes.game.game_class import GameInit
from utilities.function import init
from utilities.function import split_cards

from classes.game.game_class import GameInit
from classes.cards.card_load import CardLoad
from client.networking import Networking
from screens.abc_screen import Screen

class MainScreen(Screen):
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

        # 배경화면 생성
        self.board_image = pygame.image.load("assets/images/screens/board.png")
        self.player_board_image = pygame.image.load("assets/images/screens/player_board.png")
        self.my_board_image = pygame.image.load("assets/images/screens/my_board.png")
        self.player_state = pygame.image.load("assets/images/screens/player_state.png")

        # 컴퓨터 플레이어 1 텍스트 출력
        self.computer_player1 = "Computer 1"
        self.font_computer_player1 = pygame.font.Font(None, 30)
        self.text_computer_player1 = self.font_computer_player1.render(self.computer_player1, True, (0, 0, 0))

        # UNO 버튼 생성
        self.UNO_button_width = 100
        self.UNO_button_height = 50
        self.start_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((420, 280), (self.UNO_button_width, self.UNO_button_height)),
                text=str("UNO"),
                manager=manager
            )

        # 카드 덱 (미오픈) 이미지 로드
        self.card_back = pygame.image.load("assets/images/cards/card_back.png")
        
        # 게임 객체 생성
        self.game_init = GameInit()
        self.game_init.numPlayers = 2  # 플레이어의 수 2라고 가정

        # 게임 초기화 (카드 생성, 셔플, 맨 위 카드 꺼내기)
        init(self.game_init)

        # currentCard 객체 생성 (이미지 로드)
        self.currentCardImage = CardLoad(self.game_init.currentCard)
        
        # 카드 나눠주기
        split_cards(self.game_init)

        # user 카드 나눠주기 (이미지 로드)

        # computer 카드 나눠주기 (뒷면 이미지 로드)


    # 이벤트 처리 함수
    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            pass


    # run 함수
    def run(self, events: list[Event]) -> bool:
        
        # 화면 그리기
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.board_image, (0, 0))
        self.screen.blit(self.my_board_image, (0, 350))
        self.screen.blit(self.player_board_image, (550, 0))
        for i in range (5) :
            self.screen.blit(self.player_state, (560, 10 + i * 118))
            
        # 컴퓨터 플레이어 텍스트
        self.screen.blit(self.text_computer_player1, (570, 20))

        # 카드 덱
        self.screen.blit(self.card_back, (60, 60))

        # currentCard
        self.currentCardImage.current_card_draw(self.screen)


        for event in events:
            self.handle_event(event)

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running