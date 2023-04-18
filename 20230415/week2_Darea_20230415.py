# 지역D 스크립트

from class_20230415 import *
from function_20230415 import *

print("D지역에 오신 것을 환영합니다!")
print("컴퓨터 ai의 수를 원하는대로 늘릴 수 있는 지역입니다!")
print("-----------------------------------------------")

ess = GameInit()   #ess: class 파일 유닛
ess.numPlayers = int(input("인간을 포함한 플레이어의 수?"))   # 1명의 인간 플레이어 + 3명의 컴퓨터
print(ess.numPlayers,"명이 함께하는 우노게임을 시작합니다!")
init(ess)      #게임 초기 설정(카드 만들기, 섞기, 분배)
split_cards(ess)

ess.running = True



while ess.running:    
    
    if ess.myTurn == ess.playerTurn :
        play_game(ess, ess.playerList[ess.playerTurn])   #내턴일때
    else:
        ai_play_game(ess, ess.playerList[ess.playerTurn])   #컴퓨터턴일때
        
    game_end(ess)   #결과 출력하고 종료함
    