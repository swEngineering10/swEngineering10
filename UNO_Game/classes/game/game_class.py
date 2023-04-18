# Player 클래스 분리 아직 안한 버전

import pygame

class GameInit(object):
    def __init__(self):
        self.playerList = [[], [], [], [], [], [], []]          # 모든 플레이어의 보유 카드 정보 (최대 7명)
        self.unopenDeck = list()                                # 카드 더미
        self.openDeck = list()                                  # 오픈된 카드 더미
        self.currentCard = tuple()                              # openDeck의 가장 위 카드
        self.cardColor = ['Blue', 'Red', 'Green', 'Yellow']     # 카드 색깔 종류
        self.available = []     #가지고 있는 덱에서 낼 수 있는 카드 집합

        self.numPlayers = 0     #플레이어의 수
        self.playerTurn = 0     #현재 턴은 몇번째 턴?
        self.myTurn = 0         #내턴은 몇번째인지 저장
        self.nextTurn = 0       #다음턴은 몇번째 플레이어인가?
        self.doubleWild = 0     #Wild가 중복으로 나오는 경우 방지 이전 색깔 저장 변수
        
        self.playDirection = 1          # 게임 진행 방향
        self.currentPlayerIndex = -1    # 현재 턴인 플레이어의 인덱스

        self.isCardDrawn = False        # 카드 뽑았는지 여부
        self.isCardPlayed = False       # 카드 냈는지 여부
        self.Draw2Attack = False        # Draw2 공격이 진행중인가?
        self.Draw2Count = 0             # Draw2 공격이 몇번 중첩되었는가?
        self.turnCount = 1              # 게임이 시작된 이래로 몇번씩 주고받았는가?
        
        self.winner = 0         #승리자 저장 변수
        self.score = []     #점수 저장 변수
        
        self.smartAi = False    #지역A의 똑똑한 AI인가?
        
        self.running = True
        
        
'''class Player:
    def __init__(self, name):
        self.deck = []
        self.name = name
        '''