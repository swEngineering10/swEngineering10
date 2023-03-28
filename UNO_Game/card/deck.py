import number_card
import technical_card
import wild_card
import random
import color_change_card

class Deck:
    def __init__(self): #Constructor that creates a deck of cards.
        self.cards = []
        self.create_deck()
    def shuffle(self):  #Method that shuffles the deck of cards.
        random.shuffle(self.cards)
    def draw(self): #Method that draws a card from the deck.
        return self.cards.pop()
    def add_cards(self, cards): #Method that adds a list of cards to the deck.
        self.cards.extend(cards)
def create_number_cards(): #Method that creates a list of number cards.
    cards = []
    for color in number_card.Color:
        for value in number_card.Value:
            cards.append(number_card.NumberCard(color, value))
    return cards
def create_technical_cards(): #Method that creates a list of technical cards.
    cards = []
    for color in technical_card.Color:
        for value in technical_card.Value:
            cards.append(technical_card.TechnicalCard(color, value))
    return cards
def create_wild_cards(): #Method that creates a list of wild cards.
    cards = []
    for value in wild_card.Value:
        cards.append(wild_card.WildCard(value))
    return cards
def create_color_change_cards(): # Method that creates a list of color change cards.
    cards = []
    for value in color_change_card.Value:
        cards.append(color_change_card.ColorChangeCard(value))
    return cards
def create_deck(self): #Method that creates a deck of cards.
    self.cards = create_number_cards()
    self.cards.extend(create_technical_cards())
    self.cards.extend(create_wild_cards())
    self.cards.extend(create_color_change_cards())
    self.shuffle()