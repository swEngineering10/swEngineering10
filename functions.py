import itertools
import random
from random import randint

def pop(cards): # 덱의 가장 위 카드를 뽑아내는 함수
    return cards[-1]

def init(ob) :  # 게임 시작 시 초기화 작업을 진행하는 함수
    cardlist = ('0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9')

    ob.unopenDeck = list(itertools.product(cardlist, ob.cardColor)) # 색상별로 숫자 카드 생성 (순열 생성)
    random.shuffle(ob.unopenDeck)   # 카드 랜덤하게 섞기

    for i in range(4):  # 카드 7장씩 나누어주기
        for _ in range(7):
            ob.playerList[i].append(ob.upopenDeck.pop())
    
    ob.currentPlayerIndex = randint(0, 1)    # 시작 플레이어 랜덤 설정

    ob.openDeck.append(ob.unopenDeck.pop())  # 미오픈 덱의 첫 번째 카드 오픈 덱으로 이동
    ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장