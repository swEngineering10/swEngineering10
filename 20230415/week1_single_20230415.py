#1주차 싱글 플레이어 기능

from class_20230415 import *
from function_20230415 import *


print("싱글 플레이모드에 오신 것을 환영합니다!")
print("나와 1명의 컴퓨터와의 대결을 시작합니다!")
print("-----------------------------------------------")

ess = GameInit()   #ess: class 파일 유닛
ess.numPlayers = 2
init(ess)      #게임 초기 설정(카드 만들기, 섞기, 분배)
split_cards(ess)

ess.running = True



while ess.running:    
    
    if ess.myTurn == ess.playerTurn :
        play_game(ess, ess.playerList[ess.playerTurn])   #내턴일때
    else:
        ai_play_game(ess, ess.playerList[ess.playerTurn])   #컴퓨터턴일때
        
    game_end(ess)   #결과 출력하고 종료함
    