import pygame
import json
import math

from game_class import GameInit

# 이미지 로드 및 애니메이션을 위한 Card 클래스
class CardLoad:
    def __init__(self, card_value):
        self.screen_width, self.screen_height = resolution()
        self.card_value = card_value    # 카드의 정보 (튜플 값, ("Red", 5) 형식)
        self.image = pygame.image.load(f"assets/images/cards/{self.card_value[0]}_{self.card_value[1]}.png")  # 카드 이미지 로드
        self.image_rect = self.image.get_rect()
        self.current_card_pos = (230, 120)  # currentCard(오픈 카드)일 때 이미지 위치
        self.speed = 5  # 이동 속도
        self.spacing = 15   # myboard와 카드와의 간격
        self.cards_per_row = 7  # myboard에서 한 줄당 카드의 수
        self.x_interval = 50 # myboard에서 카드끼리의 수평 간격
        self.y_interval = 70 # myboard에서 카드끼리의 수직 간격
        self.deck_pos = [60, 60]    # 덱 좌표 (이미지 크기 맞춰서 바꾸기..)
        self.origin_pos = [60, 60]
        self.target_pos = [10, 360]

    # currentCard일 때 이미지 로드
    def current_card_draw(self, surface):
        surface.blit(self.image, self.current_card_pos)

    
    # 카드 받을 때 좌표 계산
    def card_pop_image(self, card_list):
        self.card_pos()

        self.origin_pos = self.deck_pos
        self.card_count = len(card_list) - 1

        # playerList에 있는 카드에 수에 따라 좌표 계산
        value1 = self.card_count // self.cards_per_row # 몫 0 ~ 2
        self.target_pos[1] = self.spacing + value1 * self.y_interval + self.background.board_image_size()[1]
        value2 = self.card_count % self.cards_per_row  # 나머지 0 ~ cards_per_row-1
        self.target_pos[0] = self.spacing + value2 * self.x_interval
    

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


    # myboard의 크기에 맞춰 안에 들어갈 카드의 좌표를 계산하는 함수
    def card_pos(self):
        self.background = BackGround()
        x, y = self.background.board_image_size()
        self.first_card_pos = [self.spacing, y + self.spacing]
        self.last_card_pos = [x - self.spacing - self.image.get_rect().width, y + self.spacing]
        dist = x - 2 * self.spacing - self.image.get_rect().width
        self.x_interval = dist / (self.cards_per_row - 1)




# 해상도 값에 따라 게임 배경 이미지를 다르게 설정하는 클래스
class BackGround:
    def __init__(self):
        self.screen_height = resolution()[1]
        self.resolution_type = self.resolution_type()
        self.background_image()
        # 디폴트 값 설정
        self.x_pos = 550
        self.y_pos = 350
        self.spacing = 10
        self.image_size()

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

    # 좌표 설정을 위한 이미지 사이즈 구하기
    def image_size(self):
        self.x_pos = self.game_board_image.get_rect().width
        self.y_pos = self.game_board_image.get_rect().height
    
    # 배경화면 그리기
    def background_draw(self, surface):
        surface.blit(self.game_board_image, (0, 0))
        surface.blit(self.my_board_image, (0, self.y_pos))
        surface.blit(self.player_board_image, (self.x_pos, 0))
        for i in range (5) :
            surface.blit(self.player_state_image,
                (self.x_pos + self.spacing, self.spacing + i * (self.screen_height - self.spacing) // 5))

    # game_board 이미지의 크기를 반환하는 함수
    def board_image_size(self):
        return self.game_board_image.get_rect().size


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
    self.screen.blit(pygame.image.load(r"assets\images\cards\UNO_Button.png"), self.uno_button.get_rect())
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