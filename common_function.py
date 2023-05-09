# Alplayer, game_logic에서 겹치는 함수 부분 빼낸 파일!
import random
from random import randint

#ai가 카드 색깔을 바꾸는 함수
def ai_color_change(ob):    
    print("바꿀 색깔을 1. Blue 2. Red 3.Green 4. Yellow중에서 무작위로 고릅니다.")
    newColour = randint(1, 4)
    ob.currentCard = (ob.cardColor[newColour-1], " ")
    print(ob.cardColor[newColour-1],"라는 색깔을 선택합니다!")