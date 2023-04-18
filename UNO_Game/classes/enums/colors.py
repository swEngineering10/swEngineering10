from enum import Enum # enum 모듈에서 Enum 클래스를 import 합니다.

from pygame.color import Color # pygame 모듈에서 Color 클래스를 import 합니다.


class Colors(Enum): # Colors 클래스를 정의하며, Enum 클래스를 상속합니다.
    BLACK = Color('Black')
    BLUE = Color((85, 85, 255))
    YELLOW = Color((255, 170, 0))
    RED = Color((255, 85, 85))
    GREEN = Color((0, 170, 0))
