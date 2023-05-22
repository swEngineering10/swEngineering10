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
from utility import handle_click_card

from utility import PlayerState
from utility import BackGround
from utility import CardLoad

from button import SelectColorPopup
from button import IsChanllengePopup
from button import IsSwapPopup
from button import SelectSwapPopup
from button import InfoPopup
from button import SettingButton
from button import SettingPopup

from game_class import GameInit
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
        self.game_init.numPlayers = 5  # 유저 포함 플레이어의 수 가정 (나중에 로비에서 값 받아야 함!!)

        # 카드 덱 (미오픈) 이미지 로드
        self.game_init.card_back_image = CardLoad(("card", "back"))

        # 게임 초기화 (카드 생성, 셔플, 맨 위 카드 꺼내기)
        init(self.game_init)

        # currentCard 이미지 로드 객체 생성
        self.game_init.open_deck_image_list.append(CardLoad(self.game_init.currentCard))
        self.game_init.current_card_image = self.game_init.open_deck_image_list[0]
        
        # 유저 보유 카드 리스트 모두 CardLoad 객체 생성 후 이미지 로드
        split_cards(self.game_init)
        for i in range(len(self.game_init.playerList[self.game_init.myTurn])) :
            self.game_init.my_card_list.append(CardLoad(self.game_init.playerList[self.game_init.myTurn][i]))
            self.game_init.my_card_list[i].card_pop_image(self.game_init.my_card_list)

        # computer player 이미지 객체 생성 (1 ~ numPlayers-1)
        for i in range(1, self.game_init.numPlayers) :
            self.game_init.player_deck_image_list.append(PlayerState(i))

        # 설정 버튼 & 설정 팝업
        self.setting_button = SettingButton()
        self.setting_popup = SettingPopup()
        self.setting_popup_button_list = [self.setting_popup.setting_button, self.setting_popup.start_button, self.setting_popup.continue_button, self.setting_popup.exit_button]
        

        # 아래는 모두 팝업 관련 객체 생성 #

        # 카드 선택 팝업 관련
        self.color_popup = SelectColorPopup()
        self.color_button_list = [self.color_popup.blue_button, self.color_popup.red_button, self.color_popup.green_button, self.color_popup.yellow_button]
        # 챌린지 여부 선택 팝업 관련
        self.challenge_popup = IsChanllengePopup()
        self.challenge_button_list = [self.challenge_popup.challenge_button, self.challenge_popup.giveup_button]
        # 스왑 여부 선택 팝업 관련
        self.swap_popup = IsSwapPopup()
        self.swap_popup_button_list = [self.swap_popup.swap_button, self.swap_popup.not_swap_button]
        # 스왑 선택 팝업 관련
        self.select_swap_popup = SelectSwapPopup(self.game_init)
        self.select_swap_button_list = self.select_swap_popup.swap_button_list

        # 게임 진행 정보 팝업 관련
        self.swap_notif = InfoPopup("스왑 카드가 사용되어 플레이어 둘의 덱이 바뀝니다!")
        self.not_swap_notif = InfoPopup("스왑을 하지 않고 넘어갑니다.")
        self.color_change = InfoPopup("색깔이 변경됩니다!")
        self.direction_change = InfoPopup("게임 방향이 전환됩니다!")
        self.skip_notif = InfoPopup("스킵 카드가 발동되어 턴을 하나 건너뜁니다!")
        self.fail_challenge = InfoPopup("도전에 실패했습니다! 다음 플레이어가 6장을 받습니다.")
        self.success_challenge = InfoPopup("도전에 성공했습니다! 현재 플레이어가 4장을 받습니다.")
        self.giveup_challenge = InfoPopup("도전을 포기합니다. 다음 플레이어가 4장을 받습니다.")


    
    # 카드 덱
    def deck_image_load(self):
        self.game_init.card_back_image.card_load(self.screen, self.game_init.card_back_image.deck_pos)

    def current_card_load(self):
        self.game_init.current_card_image.card_load(self.screen, self.game_init.card_back_image.current_card_pos)

    # currendtCard 애니메이션
    def current_card_ani(self):
        for i in range(len(self.game_init.open_deck_image_list)):
            self.game_init.open_deck_image_list[i].animation_control(self.screen)

    # 유저 플레이어 카드 로드
    def user_card_load(self):
        for i in range(len(self.game_init.my_card_list)):
            self.game_init.my_card_list[i].animation_control(self.screen)
    
    # 컴퓨터 플레이어 카드 로드
    def player_card_load(self):
        for i in range(len(self.game_init.player_deck_image_list)) :
            self.game_init.player_deck_image_list[i].player_state_draw(self.screen)

    # run 함수
    def run(self, events: list[Event]) -> bool:

        # 배경화면
        self.background.background_draw(self.screen)

        # 기타 이미지 로드
        self.deck_image_load()
        self.user_card_load()
        self.player_card_load()
        self.current_card_ani()

        # 설정 버튼 로드
        self.setting_button.draw(self.screen)


        for event in events:
            # 내 차례일 때만 카드 클릭할 수 있도록 하기
            if self.game_init.playerTurn == self.game_init.myTurn :
                handle_click_card(event, self.game_init, self.screen)

            # 설정 버튼 이벤트
            self.setting_button.handle_event(event, self.game_init, self.screen)
            if self.game_init.isPaused :
                for setting_popup_button in self.setting_popup_button_list:
                    setting_popup_button.handle_event(event, self.game_init, self.screen)

            # 아래는 팝업 이벤트
            if self.game_init.currentPopup == "color_change":
                for color_button in self.color_button_list:
                    color_button.handle_event(event, self.game_init, self.screen)
            
            if self.game_init.currentPopup == "challenge":
                for challenge_button in self.challenge_button_list:
                    challenge_button.handle_event(event, self.game_init, self.screen)

            if self.game_init.currentPopup == "is_swap":
                for swap_button in self.swap_popup_button_list:
                    swap_button.handle_event(event, self.game_init, self.screen)

            if self.game_init.currentPopup == "select_swap":
                for select_swap_button in self.select_swap_button_list:
                    select_swap_button.handle_event(event, self.game_init, self.screen)


        # 게임 실행
        if self.game_init.isPaused == False :
            if self.game_init.myTurn == self.game_init.playerTurn :
                if self.game_init.delay == 200 :
                    play_game(self.game_init, self.game_init.playerList[self.game_init.playerTurn])
                    self.game_init.delay = 0
            else:
                # 컴퓨터 플레이어 딜레이 주기
                if self.game_init.delay == 300 :
                    ai_play_game(self.game_init, self.game_init.playerList[self.game_init.playerTurn])
                    self.game_init.delay = 0


        # 이미지 새로 세팅 후 팝업창 띄우기
        if (self.game_init.delay == 150) and self.game_init.isAIPlayed :

            # currentCard의 색깔 바꾸기
            if self.game_init.currentCard[1] == "Color_Change" :
                print("색깔 변경")
                self.game_init.current_card_image.image = pygame.image.load(f"assets/images/cards/{self.game_init.currentCard[0]}_Color_Change.png")
                self.game_init.alertType = "color_change"   # 알림창 띄우기

            elif self.game_init.currentCard[1] == "Draw4" :
                self.game_init.current_card_image.image = pygame.image.load(f"assets/images/cards/{self.game_init.currentCard[0]}_Draw4.png")
                self.game_init.alertType = "color_change"   # 알림창 띄우기

            elif self.game_init.currentCard[1] == "Swap" : 
                self.game_init.current_card_image.image = pygame.image.load(f"assets/images/cards/{self.game_init.currentCard[0]}_Swap.png")
                self.game_init.alertType = "color_change"   # 알림창 띄우기

            self.game_init.isAIPlayed = False

        # 게임 중단이 아닌 경우에만 delay 증가
        if self.game_init.isPaused == False :
            self.game_init.delay += 1

        
        # 팝업 로드
        if self.game_init.isPaused :    # 설정
            self.setting_popup.popup_draw(self.screen)

        if self.game_init.currentPopup == "color_change" :
            self.color_popup.popup_draw(self.screen)
        elif self.game_init.currentPopup == "challenge" :
            self.challenge_popup.popup_draw(self.screen)
        elif self.game_init.currentPopup == "is_swap" :
            self.swap_popup.popup_draw(self.screen)
        elif self.game_init.currentPopup == "select_swap" :
            self.select_swap_popup.popup_draw(self.screen)
        
        
        # 알림창 로드
        if self.game_init.alertType != None :
            self.game_init.alertDelay += 1
            if self.game_init.alertType == "swap" :
                self.swap_notif.popup_draw(self.screen)
            elif self.game_init.alertType == "not_swap" :
                self.not_swap_notif.popup_draw(self.screen)
            elif self.game_init.alertType == "color_change" :
                self.color_change.popup_draw(self.screen)
            elif self.game_init.alertType == "direction_change" :
                self.direction_change.popup_draw(self.screen)
            elif self.game_init.alertType == "skip" :
                self.skip_notif.popup_draw(self.screen)
            elif self.game_init.alertType == "fail_challenge" :
                self.fail_challenge.popup_draw(self.screen)
            elif self.game_init.alertType == "success_challenge" :
                self.success_challenge.popup_draw(self.screen)
            elif self.game_init.alertType == "giveup_challenge" :
                self.giveup_challenge.popup_draw(self.screen)

            # 알림창 일정 시간이 지나면 없어지도록 설정
            if self.game_init.alertDelay >= 200 :
                self.game_init.alertType = None
                self.game_init.alertDelay = 0
        

        if self.networking.current_game.is_started:
            self.is_running = False
        return self.is_running