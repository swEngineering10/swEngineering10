# 지역C 스크립트

from class_20230415 import *
from function_20230415 import *

print("C지역에 오신 것을 환영합니다!")
print("C지역은 매 5턴마다 낼 수 있는 카드의 색상이 무작위로 변경됩니다!!")
print("나와 2명의 컴퓨터 플레이어와의 대결을 시작합니다!")
print("-----------------------------------------------")

ess = GameInit()   #ess: class 파일 유닛
ess.numPlayers = 3   # 1명의 인간 플레이어 + 2명의 컴퓨터
init(ess)      #게임 초기 설정(카드 만들기, 섞기, 분배)
split_cards(ess)

ess.running = True



while ess.running:    
    if ess.turnCount == 1:
        pass
    elif ess.turnCount % 5 == 1:
        print("\n")
        print("**5턴이 지났으므로 랜덤의 색상으로 변경됩니다!**")
        ai_color_change(ess)
        print("\n")
        time.sleep(3)
        
    if ess.myTurn == ess.playerTurn :
        play_game(ess, ess.playerList[ess.playerTurn])   #내턴일때
    else:
        ai_play_game(ess, ess.playerList[ess.playerTurn])   #컴퓨터턴일때
        
    game_end(ess)   #결과 출력하고 종료함
    