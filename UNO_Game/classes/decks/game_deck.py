from collections import deque

from classes.cards.card import Card
from utilities.card_utility import random_cards


class GameDeck:
    def __init__(self, maxsize: int = 1):
        self.cards = deque([], maxsize)

    def append_card(self, card: Card, ignore: bool = False) -> bool:
        if ignore or card.possible_move(self.cards[0]):
            self.cards.appendleft(card)
            return True
        else:
            return False 

    def init_random(self):
        self.cards.appendleft(random_cards(1)[0])
