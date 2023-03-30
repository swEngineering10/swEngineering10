# 파이썬 버전 상관없게 해줌
#from __future__ import annotations
#파이썬 3.7에서 dataclasses라는 매우 매력적인 모듈이 표준 라이브러리에 추가
from dataclasses import dataclass, field

from classes.enums.colors import Colors

@dataclass
class Card:
    color: Colors
    nominal: int = field(init=False)

    def possible_move(self, card: Card) -> bool:
        if card.color == self.color:
            return True
        else:
            return False
        
    @staticmethod
    def move(game):
        pass