# 3월 31일 새벽 1시까지 한 것 병합만 한 버전
# 우노 작업이랑 타이머 작업은 아직 미구현
# 도식화 진행중!! 완료되면 업로드 예정!

from class_20230404 import *
from function_20230404 import *


ess = GameInit()   #ess: class 파일 유닛
init(ess)      #게임 초기 설정(카드 만들기, 섞기, 분배)


#디버그용
'''for i in range(0, 5):
    print("plyer[", i, "]: ", ess.playerList[i])

print("현재 카드: ", ess.currentCard)'''

ess.running = True



#디버그용으로 한거임
while ess.running:    
    
    if ess.myTurn == ess.playerTurn :
        play_game(ess, ess.playerList[ess.playerTurn])   #내턴일때
    else:
        ai_play_game(ess, ess.playerList[ess.playerTurn])   #컴퓨터턴일때
        
    game_end(ess)   #결과 출력하고 종료함
    




