# 지역D 스크립트
# 지역D 명세서
'''
## 1. 스토리 명칭
* Stage 4

## 2. 스토리 요약
* 플레이어가 플레이 유저의 수를 정해서 플레이 할 수 있다.

## 3. 목표
* 플레이어가 AI들을 상대로 이겨야 한다.

## 4. 규칙
* 전반적인 규칙은 UNO게임과 일치한다.
* 일반적인 UNO게임은 플레이어 유저수가 정해져 있지만 4스테이지에서는 유저수를 지정해서 플레이 할 수 있다.

## 5. 요구사항
* 플레이어와 컴퓨터의 패는 게임 시작 시 무작위로 생성되어야 한다.
* 카드는 무작위로 드로우 되어야 한다.
* 게임 종료가 특정조건에 따라 표시되어야 한다.
* 플레이어의 수를 지정을 하고, 반영할 수 있어야 한다.

## 6. 제약사항
* 컴퓨터는 무작위로 카드를 내어야 한다.
* 게임 플레이 도중 꼼수는 허락할 수 없다.

## 7. 테스트
* 콘솔창으로 계속 카드들의 상태를 볼 수 있어야 한다.
* 꼼수가 있는지 여러 방법으로 테스트를 해야한다.





'''





import sys
from class_20230415 import *
from function_20230415 import *

print("D지역에 오신 것을 환영합니다!")
print("컴퓨터 ai의 수를 원하는대로 늘릴 수 있는 지역입니다!")
print("-----------------------------------------------")

ess = GameInit()   #ess: class 파일 유닛
ess.numPlayers = int(input("인간을 포함한 플레이어의 수?"))   # 1명의 인간 플레이어 + 3명의 컴퓨터
if ess.numPlayers == 1:
    print("플레이어수가 1명이라 게임이 종료됩니다!")
    sys.exit()
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
    