# 3월 24일까지 한 것 병합만 한 버전
# 메인 파일, function, class파일 분리 버전
# 플레이어 순서, 플레이어 클래스 분리, 타이머 부분 아직 손 안본 버전

from class_20230324 import *
from function_20230324 import *


ess = GameInit()   #ess: class 파일 유닛
init(ess)      #게임 초기 설정(카드 만들기, 섞기, 분배)


#디버그용
#플레이어가 4명으로 가정되어 있는 버전임
'''for i in range(0, 5):
    print("plyer[", i, "]: ", ess.playerList[i])

print("현재 카드: ", ess.currentCard)'''
print("현재 순서: ", ess.currentPlayerIndex)



#디버그용으로 한거임
play_game(ess, ess.playerList[0])   #나

ai_play_game(ess, ess.playerList[1])   #컴퓨터

play_game(ess, ess.playerList[0])   #나



