# Alplayer, game_logic에서 겹치는 함수 부분 빼낸 파일!
import pygame

import random
from random import randint
from utility import CardLoad

#ai가 카드 색깔을 바꾸는 함수
def ai_color_change(ob):    
    newColour = randint(1, 4)   # 색깔 무작위로 선택

    # currentCard의 색깔 바꾸기
    if ob.currentCard[1] == "Color_Change" :
        ob.currentCard = (ob.cardColor[newColour-1], "Color_Change")
    elif ob.currentCard[1] == "Draw4" :
        ob.currentCard = (ob.cardColor[newColour-1], "Draw4")
    elif ob.currentCard[1] == "Swap" : 
        ob.currentCard = (ob.cardColor[newColour-1], "Swap")

    ob.colorDelay = 0    
    ob.currentPopup = None
    ob.IsChallenge = None
    ob.isUnChecked = True
    ob.isUnChecked0 = True


#다음 playerTurn턴 정할 때 숫자가 넘치지 않나 검사하는 함수
def over_turn(ob):
    if ob.playerTurn == ob.numPlayers + 2:
        ob.playerTurn = 2
    elif ob.playerTurn == ob.numPlayers + 1:
        ob.playerTurn = 1
    elif ob.playerTurn == ob.numPlayers:
        ob.playerTurn = 0
    elif ob.playerTurn == -1:
        ob.playerTurn = ob.numPlayers - 1
    elif ob.playerTurn == -2:
        ob.playerTurn = ob.numPlayers - 2