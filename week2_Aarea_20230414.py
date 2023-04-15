# 지역B 스크립트

from class_20230414 import *
from function_20230414 import *

print("A지역에 오신 것을 환영합니다!")
print("나와 3명의 컴퓨터 플레이어와의 대결을 시작합니다!")
print("-----------------------------------------------")

ess = GameInit()   #ess: class 파일 유닛
ess.numPlayers = 4   # 1명의 인간 플레이어 + 3명의 컴퓨터
init(ess)      #게임 초기 설정(카드 만들기, 섞기, 분배)

ess.running = True



while ess.running:    
    
    if ess.myTurn == ess.playerTurn :
        play_game(ess, ess.playerList[ess.playerTurn])   #내턴일때
    else:
        ai_play_game(ess, ess.playerList[ess.playerTurn])   #컴퓨터턴일때
        
    game_end(ess)   #결과 출력하고 종료함
    