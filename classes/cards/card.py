from __future__ import annotations # from future import annotations : 이 코드는 Python 3.7 이하 버전에서 발생하는 순환 참조 문제를 해결하기 위해 Python 3.7 이상의 버전에서 사용할 수 있는 future 모듈의 annotations 기능을 import 합니다.

from dataclasses import dataclass, field

from classes.enums.colors import Colors


@dataclass
class Card:
    color: Colors # color는 객체명이며, Colors는 클래스명입니다.
    nominal: int = field(init=False) # 카드의 숫자를 결정.  이 변수는 init=False로 설정되어 생성자에서 초기화되지 않습니다.

    def possible_move(self, card: Card) -> bool: # 카드의 색이 같으면 이동이 가능한지 여부를 반환하는 메서드. -> 뒤에 오는 것은 이 함수의 반환값의 자료형을 나타냄.
        if card.color == self.color:
            return True
        else:
            return False

    # static 메소드: 클래스의 인스턴스 없이 호출 가능한 메소드. 즉 클래스 수준의 동작을 정의하는 메소드. 이 메소드는 인스턴스 변수에 접근할 필요가 없기 때문에 정적 메소드로 정의됩니다.
    @staticmethod # game 매개변수를 받아 이동(move)을 구현하는 move 메서드를 정의합니다. 현재는 pass로 구현되어 있어서 아무런 동작도 하지 않습니다.
    def move(game):
        pass
