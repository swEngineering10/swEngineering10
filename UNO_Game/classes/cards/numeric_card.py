from dataclasses import dataclass

from classes.cards.card import Card


@dataclass
class NumericCard(Card):
    number: int

    def __post_init__(self):
        self.nominal = self.number

    def possible_move(self, card: Card) -> bool:
        # super()는 Card 클래스를 말함. 색이 같거나, 숫자가 같으면 이동이 가능하다.
        # hassattr(object, name) 객체가 name이라는 속성을 가지고 있다면 true, 아니면 false 반환.
        # 즉 비교 대상 카드가 숫자 카드인 경우 현재 카드와 비교 대상 카드의 숫자가 같은지 여부를 확인하는 코드입니다.
        if super().possible_move(card) or (hasattr(card, 'number') and card.number == self.number):
            return True
        else:
            return False
