import pygame
import pygame_gui
import random

pygame.init()
pygame.display.set_caption('UNO')

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
background_image1 = pygame.image.load('screens/board.png')
background_image2 = pygame.image.load('screens/player_board.png')
background_image3 = pygame.image.load('screens/my_board.png')
clock = pygame.time.Clock()

# 이미지 로드 및 애니메이션을 위한 Card 클래스


class CardLoad:
    def __init__(self, card_value):
        self.card_value = card_value    # 카드의 정보 (튜플 값, ("Red", 5) 형식)
        print(self.card_value)  # 디버깅용 (로드 이미지랑 비교)
        self.image = pygame.image.load(
            f"assets/images/cards/{self.card_value[0]}_{self.card_value[1]}.png")  # 카드 이미지 로드
        self.current_card_pos = (230, 120)  # currentCard(오픈 카드)일 때 이미지 위치

    # currentCard일 때 이미지 로드

    def current_card_draw(self, surface):
        surface.blit(self.image, self.current_card_pos)


card_images = {}
suits = ['Blue', 'Yellow', 'Red', 'Green']
items = ['All_In', 'Draw2', 'Reverse', 'Skip']
wilds = ['Color_Change', 'Draw4', 'Swap']
for suit in suits:
    for rank in range(0, 9):
        card_name = suit + '_' + str(rank)
        filename = 'cards/' + card_name + '.png'
        card_images[card_name] = pygame.image.load(filename)
    for item in items:
        card_name = suit + '_' + item
        filename = 'cards/' + card_name + '.png'
        card_images[card_name] = pygame.image.load(filename)
for wild in wilds:
    card_name = 'Wild_' + wild
    filename = 'cards/' + card_name + '.png'
    card_images[card_name] = pygame.image.load(filename)


class Card:

    def __init__(self, name):
        self.name = name
        self.image = card_images[name]


class Deck:
    def __init__(self):
        self.cards = []
        for card_name in card_images.keys():
            card = Card(card_name)
            self.cards.append(card)
        random.shuffle(self.cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


def distribute_cards(deck, players):
    num_players = len(players)
    num_cards = len(deck.cards)
    cards_per_player = 7

    for i, player in enumerate(players):
        start_index = i * cards_per_player
        end_index = start_index + cards_per_player
        player.hand = deck.cards[start_index: end_index]

    remaining_cards = num_cards % num_players
    if remaining_cards > 0:
        extra_cards = deck.cards[-remaining_cards:]
        random_player = random.choice(players)
        random_player.hand += extra_cards


def draw_cards(players):
    card_width = card_images['Blue_1'].get_width() * 0.6
    card_height = card_images['Blue_1'].get_height() * 0.6

    x_offset = screen_width * 0.1
    y_offset = screen_height * 0.7

    for i, player in enumerate(players):
        for j, card in enumerate(player.hand):
            x = x_offset + j * card_width
            y = y_offset + i * card_height * 1.5
            screen.blit(card.image, (x, y))


def game_loop():
    deck = Deck()
    player1 = Player('Player 1')
    players = [player1]

    distribute_cards(deck, players)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image1, (0, 0))
        screen.blit(background_image3,
                    (screen_width * 0.001, screen_height * 0.6))
        screen.blit(background_image2,
                    (screen_width * 0.7, screen_height * 0.001))
        draw_cards(players)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


game_loop()
