import pygame
import json
import math

<<<<<<< HEAD
from game_class import *
from game_logic import *

=======
>>>>>>> 567d3181f12ca04a4c9556af0ab21bee9df8f2b2
# 이미지 로드 및 애니메이션을 위한 Card 클래스
class CardLoad:
    def __init__(self, card_value):
        self.screen_width, self.screen_height = resolution()
        self.card_value = card_value    # 카드의 정보 (튜플 값, ("Red", 5) 형식)
        self.image = pygame.image.load(f"assets/images/cards/{self.card_value[0]}_{self.card_value[1]}.png")  # 카드 이미지 로드
        self.image_rect = self.image.get_rect()
        self.background = BackGround()  # BackGround 객체 생성
        self.current_card_pos = self.opendeck_image_pos()  # currentCard(오픈 카드)일 때 이미지 위치
        self.deck_pos = self.deck_image_pos()    # 덱 좌표
        self.speed = 5  # 이동 속도
        self.spacing = 15   # myboard와 카드와의 간격
<<<<<<< HEAD
        self.cards_per_row = 12  # myboard에서 한 줄당 카드의 수
        self.x_interval = self.background.card_pos(self.background.my_board_image.get_rect().size,
                        self.spacing, self.image, self.cards_per_row) # myboard에서 카드끼리의 수평 간격
        self.y_interval = 70 # myboard에서 카드끼리의 수직 간격
        self.position = self.deck_pos  # 현재 position
        self.origin_pos = [60, 60]
        self.target_pos = [10, 360]

        self.back_pos()


    def back_pos(self) :
        if self.card_value == ("card", "back") :
            self.image_rect.left, self.image_rect.top = self.deck_pos

    # 카드 이미지 로드
    def card_load(self, surface, pos):
=======
        self.cards_per_row = 7  # myboard에서 한 줄당 카드의 수
        self.x_interval = self.background.card_pos(self.background.my_board_image.get_rect().size,
                        self.spacing, self.image, self.cards_per_row) # myboard에서 카드끼리의 수평 간격
        self.y_interval = 70 # myboard에서 카드끼리의 수직 간격
        self.position = [0, 0]  # 현재 position
        self.origin_pos = [60, 60]
        self.target_pos = [10, 360]


    # 카드 이미지 로드
    def card_draw(self, surface, pos):
>>>>>>> 567d3181f12ca04a4c9556af0ab21bee9df8f2b2
        surface.blit(self.image, pos)

    
    # 카드 받을 때 좌표
    def card_pop_image(self, card_list):

        self.origin_pos = self.deck_pos
        self.card_count = len(card_list) - 1

        # playerList에 있는 카드에 수에 따라 좌표 계산
        value1 = self.card_count // self.cards_per_row # 몫 0 ~ 2
        y_pos = self.spacing + value1 * self.y_interval + self.background.board_image_size()[1]
        value2 = self.card_count % self.cards_per_row  # 나머지 0 ~ cards_per_row - 1
        x_pos = self.spacing + value2 * self.x_interval

        self.target_pos = [x_pos, y_pos]
<<<<<<< HEAD
        self.position = self.target_pos     # 현재 좌표 설정
=======
        self.position = self.target_pos
>>>>>>> 567d3181f12ca04a4c9556af0ab21bee9df8f2b2
    

    # 이미지 애니메이션
    def image_animation(self, surface):
        self.image_rect.x = self.origin_pos[0]
        self.image_rect.y = self.origin_pos[1]

        # 이동할 좌표 간의 거리를 계산
        self.dx = self.target_pos[0] - self.origin_pos[0]
        self.dy = self.target_pos[1] - self.origin_pos[1]
        distance = math.sqrt(self.dx**2 + self.dy**2)  # 두 좌표 사이의 거리

        self.move_x = self.speed * self.dx / distance  # x축 이동 거리
        self.move_y = self.speed * self.dy / distance  # y축 이동 거리

        self.origin_pos[0] += self.move_x
        self.origin_pos[1] += self.move_y

        self.image_rect.x = int(self.origin_pos[0])
        self.image_rect.y = int(self.origin_pos[1])

        surface.blit(self.image, self.image_rect)

<<<<<<< HEAD
    # 카드 내는 함수
    def play_card_event(self, surface):
        self.origin_pos = self.position
        self.target_pos = self.current_card_pos
        self.image_animation(surface)    # 애니메이션 (문제있음)
        self.position = self.target_pos

=======
    
    # 카드 선택됐을 때 이미지 처리 (조금 위로 가게 함!)
    def card_select(self, surface):
        self.origin_pos = self.position # 현재 좌표를 origin 좌표에 대입
        # target 좌표는 현재 좌표에서 y좌표만 변경
        self.target_pos[0] = self.position[0]
        self.target_pos[1] = self.position[1] + 10

        # 애니메이션 효과
        self.image_animation(surface)

>>>>>>> 567d3181f12ca04a4c9556af0ab21bee9df8f2b2

    # 색깔을 바꾼 경우 바꾼 색깔과 current_card 객체를 받아 카드 색깔을 바꿈
    def color_change(self, current_card, color):
        value1 = current_card.card_value[0]
        value2 = current_card.card_value[1]
        self.image = pygame.image.load(f"assets/images/cards/{value1}_{value2}_{color}.png")
<<<<<<< HEAD
        self.card_load(self.position)
=======
        self.card_draw(self.position)
>>>>>>> 567d3181f12ca04a4c9556af0ab21bee9df8f2b2

    # deck (unopendeck)의 이미지 좌표 계산
    def deck_image_pos(self):
        x, y = self.background.board_image_size()
        width, height = self.image.get_rect().size
        x_pos = (x  - width) * 0.2
        y_pos = (y - height) * 0.3
        return [x_pos, y_pos]


    # opendeck의 이미지 좌표 계산
    def opendeck_image_pos(self):
        x, y = self.background.board_image_size()
        width, height = self.image.get_rect().size
        return [x // 2 - width // 2, y // 2 - height // 2]


# user (나) 이외의 플레이어 상태를 로드해주는 클래스 (player_num : 플레이어 번호)
class PlayerState:
    def __init__(self, player_num):
        self.player_bg = BackGround()
        self.player_num = player_num
        self.player_name = "Computer " + str(player_num)
        self.player_pos = self.player_pos_change()
        self.player_card_num = 7    # 가지고 있는 카드의 개수
        self.player_cards_per_row = 10    # 한 줄당 카드의 개수
        self.player_spacing = 5
        self.image = pygame.image.load("assets/images/cards/card_back_player.png")  
        self.player_name_font = pygame.font.Font(None, 30)
        self.player_name_text = self.player_name_font.render(self.player_name, True, (0, 0, 0))
        self.player_x_interval = self.player_bg.card_pos(self.player_bg.player_state_image.get_rect().size,
                        self.player_spacing, self.image, self.player_cards_per_row) # player_board에서 카드끼리의 수평 간격
        self.player_y_interval = 20
        

    # 플레이어 state 박스의 좌표 구하기 (플레이어 번호에 따라 달라짐)
    def player_pos_change(self):
        x = self.player_bg.x_pos + self.player_bg.state_spacing
        y = self.player_bg.state_spacing
        interval = self.player_bg.player_state_image.get_rect().height + self.player_bg.state_spacing
        return [x, y + (self.player_num - 1) * interval]

    # 플레이어 상태 이미지 로드 (애니메이션 없다고 가정,,,)
    def player_state_draw(self, surface):
        # 플레이어 이름 로드
        text_draw_pos = [self.player_pos[0] + self.player_spacing, self.player_pos[1] + self.player_spacing]
        surface.blit(self.player_name_text, text_draw_pos)    

        # 플레이어의 가장 첫 번째 카드 좌표
        card_draw_pos = [text_draw_pos[0], text_draw_pos[1] + self.player_name_text.get_size()[1] + self.player_spacing]

        # 플레이어 카드 로드
        for i in range (self.player_card_num):
            if (i % self.player_cards_per_row == 0)  & (i > 1):
                card_draw_pos[0] = text_draw_pos[0]
                card_draw_pos[1] += self.player_y_interval
            surface.blit(self.image, (card_draw_pos[0] + (i % self.player_cards_per_row) * self.player_x_interval, card_draw_pos[1]))

    # 우노 상태일 때 우노 이미지 로드



# 해상도 값에 따라 게임 배경 이미지를 다르게 설정하는 클래스
class BackGround:
    def __init__(self):
        self.screen_height = resolution()[1]
        self.resolution_type = self.resolution_type()
        self.background_image()
        # 게임 보드 크기
        self.x_pos = self.game_board_image.get_rect().width
        self.y_pos = self.game_board_image.get_rect().height
        self.state_spacing = 10

    # 해상도 타입을 int 타입으로 반환 (이미지 파일 이름 설정 목적)
    def resolution_type(self):
        if resolution()[0] == 640 : 
            return 1
        elif resolution()[0] == 800 :
            return 2
        else : 
            return 3

    def background_image(self):
        self.game_board_image = pygame.image.load(f"assets/images/screens/game_board{self.resolution_type}.png")
        self.my_board_image = pygame.image.load(f"assets/images/screens/my_board{self.resolution_type}.png")
        self.player_board_image = pygame.image.load(f"assets/images/screens/player_board{self.resolution_type}.png")
        self.player_state_image = pygame.image.load(f"assets/images/screens/player_state{self.resolution_type}.png")
    
    # 배경화면 그리기
    def background_draw(self, surface):
        surface.blit(self.game_board_image, (0, 0))
        surface.blit(self.my_board_image, (0, self.y_pos))
        surface.blit(self.player_board_image, (self.x_pos, 0))
        for i in range (5) :
            surface.blit(self.player_state_image,
                (self.x_pos + self.state_spacing, self.state_spacing + i * (self.screen_height - self.state_spacing) // 5))

    # game_board 이미지의 크기를 반환하는 함수
    def board_image_size(self):
        return self.game_board_image.get_rect().size

    # myboard의 크기에 맞춰 안에 들어갈 카드의 좌표를 계산하는 함수
    def card_pos(self, board_size, spacing, card_image, cards_per_row):
        x = board_size[0]
        # first_card_pos = [spacing, y + spacing]
        # last_card_pos = [x - spacing - card_image.get_rect().width, y + spacing]
        dist = x - 2 * spacing - card_image.get_rect().width
        x_interval = dist / (cards_per_row - 1)
        return x_interval


# 해상도 값을 json 파일로부터 불러와 튜플로 반환하는 함수
def resolution():
    with open('display_config.json', 'r') as f:
        config_data = json.load(f)
    return (config_data['resolution']['width'], config_data['resolution']['height'])



'''
def exit_button(self):
    self.mixer.music.stop()
    print('종료 버튼을 눌러 게임이 종료되었습니다!')
    self.running = False

def draw(self):
    self.screen.blit(pygame.image.load(r"assets/images/cards/UNO_Button.png"), self.uno_button.get_rect())
'''
    
# 카드 클릭 이벤트
############# 바꿔야함!!!!!!!! ################
def get_clicked_card(cards, x, y, spacing, mouse_x, mouse_y, max_per_row):
    for i, card in enumerate(cards):
        card_width, card_height = card.card_img.get_size()
        row = i // max_per_row
        column = i % max_per_row
        card_x = x + column * spacing
        card_y = y + row * (spacing + 10)  # 각 행의 시작 y 좌표를 고려하도록 수정
        if card_x <= mouse_x < card_x + card_width and card_y <= mouse_y < card_y + card_height:
            return i, card
    return None, None


def card_click(my_card_list, game_init, card_back, mouse_pos, surface):
    # 카드를 받는 경우
    if card_back.image_rect.collidepoint(mouse_pos):
        print("카드를 받습니다.")
        game_init.PlayedCard = 0
        game_init.isCardPlayed = True
    # 카드를 내는 경우
    else :
        # 겹치는 부분 중복 선택이 되지 않기 위해 가장 위쪽 카드 하나만 선택
        for i in range (len(my_card_list)-1, -1, -1) :
            if my_card_list[i].image_rect.collidepoint(mouse_pos):
                if my_card_list[i].card_value in game_init.available:   # 낼 수 있는 카드일 경우
                    print(str(my_card_list[i].card_value) + "카드 클릭")
                    clicked_card = my_card_list[i]
                    clicked_card.play_card_event(surface)   # 해당 카드 클릭 이벤트 실행
                    game_init.PlayedCard = i + 1
                    my_card_list.pop(i)     # 리스트에서 제외
                    game_init.isCardPlayed = True
                    break
                break
        