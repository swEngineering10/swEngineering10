from dataclasses import dataclass


from classes.decks.game_deck import GameDeck
from classes.enums.directions import Directions


@dataclass
class Game:
    deck: GameDeck
    cur_user_index: int = 0 #랜덤으로 바꿔야함.
    direction: Directions = Directions.CLOCKWISE

    def append_user(self):
        if len(self.users) <= 4:
            print(self.users)
        else:
            raise ValueError("최대 4인까지 플레이 가능합니다.")

    @property
    def is_started(self) -> bool:
        return True if len(self.users) == 4 else False

    def next_player(self):
        if self.direction == Directions.CLOCKWISE:
            if self.cur_user_index != 3:
                self.cur_user_index += 1
            else:
                self.cur_user_index = 0
        elif self.direction == Directions.COUNTER_CLOCKWISE:
            if self.cur_user_index != 0:
                self.cur_user_index -= 1
            else:
                self.cur_user_index = 3
