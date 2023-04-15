#1주차 싱글 플레이어 기능

from class_20230414 import *
from function_20230414 import *

ess = GameInit()   #ess: class 파일 유닛
ess.numPlayers = int(input("나를 포함한 플레이어의 수는 몇명입니까? "))
init(ess)      #게임 초기 설정(카드 만들기, 섞기, 분배)

ess.running = True



while ess.running:    
    
    if ess.myTurn == ess.playerTurn :
        play_game(ess, ess.playerList[ess.playerTurn])   #내턴일때
    else:
        ai_play_game(ess, ess.playerList[ess.playerTurn])   #컴퓨터턴일때
        
    game_end(ess)   #결과 출력하고 종료함
    