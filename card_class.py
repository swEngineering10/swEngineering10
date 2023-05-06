import pygame
import random
import sys

# 카드 클래스
class Card:
    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = position

# 초기화
pygame.init()

# 게임 창 생성
screen = pygame.display.set_mode((800, 600))

# 카드 이미지 로드
card_image = pygame.image.load('assets/images/back.png')

# 플레이어 클래스
class Player:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

# 카드를 플레이어에게 나눠주는 함수
def deal_cards(player):
    for _ in range(7):
        random_position = (random.randint(0, 800 - card_image.get_width()), random.randint(0, 600 - card_image.get_height()))
        card = Card(card_image, random_position)
        player.add_card(card)

# 플레이어 객체 생성
player = Player()

# 카드를 플레이어에게 나눠줌
deal_cards(player)

# 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 이벤트 처리
            for card in player.cards:
                if card.rect.collidepoint(event.pos):
                    print("카드를 클릭했습니다!")
                    player.remove_card(card)

    # 그리기
    screen.fill((0, 0, 0))
    for card in player.cards:
        screen.blit(card.image, card.rect)
    pygame.display.flip()

