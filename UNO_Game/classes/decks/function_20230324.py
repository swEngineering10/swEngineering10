#카드 섞기, 플레이어 게임 진행, ai 게임 진행 함수까지 구현
#기술카드 미구현 버전
#와일드 카드 판별도 아직 미구현 버전!


import itertools
import random
from random import randint
import time


def pop(cards): # 덱의 가장 위 카드를 뽑아내는 함수
    return cards[-1]        
        

def init(ob) :      #게임 초기화 함수

    #혹시 몰라서 놔두는 친구들, 무시해도 ok

    '''cardlist = ('0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9')

    ob.unopenDeck = list(itertools.product(cardlist, ob.cardColor)) # 색상별로 숫자 카드 생성 (순열 생성)
    random.shuffle(ob.unopenDeck)   # 카드 랜덤하게 섞기
    '''
    
    ob.unopenDeck = []   #unopenDeck: 오픈 안한 모든 카드 집합
    colours = ["Red", "Yellow", "Blue", "Green"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Skip", "Reverse", "Draw_Two", "All_In"]
    #values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "Skip", "Reverse", "Draw_Two", "All_In"]
    Wild = ["Color_Change", "Draw4", "Swap"]
   
    for colour in colours:      #컬러카드 생성
        for value in values:
            count_card = (colour, value)
            #count_card.append((colour, value))
            #count_card = "{} {}".format(colour, value)
            ob.unopenDeck.append(count_card)
            if value!=0:
                ob.unopenDeck.append(count_card)
                
    for i in Wild:      #와일드카드 생성
        for j in range(4):
            ob.unopenDeck.append(('Wild', i))
            
    random.shuffle(ob.unopenDeck)   # 카드 랜덤하게 섞기
    
    
    ###### 4명의 플레이어로 가정한거임!!!!! #######
    for i in range(4):  # 카드 7장씩 나누어주기
        for _ in range(7):
            ob.playerList[i].append(ob.unopenDeck.pop())
            
    ### ??????????????? ###
    ob.currentPlayerIndex = randint(0, 1)    # 시작 플레이어 랜덤 설정

    ob.openDeck.append(ob.unopenDeck.pop())  # 미오픈 덱의 첫 번째 카드 오픈 덱으로 이동
    ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
    
    
    
    
def play_game(ob, cards):       #플레이어 게임 진행 함수
    
    print("\n\n")
    
    available = []          #available: 가지고 있는 덱에서 낼 수 있는 카드 집합
    for card in cards:
        if (card[0] == ob.currentCard[0] or card[1] == ob.currentCard[1] or card[0] == 'Wild'):     #낼 수 있는 카드 판별
            available.append(card)
    print("놓여진 카드: ", ob.currentCard)       #아래부터 나오는 print들은 다 디버그용
    print("내가 낼 수 있는 카드: ", available)
    
    #아직 파이게임으로 구현 못하므로 콘솔창 형태로 제작함
    
    #디버그용. pygame 구현시 마우스 터치 이런형태로 바꿔야함
    a = int(input("몇번째 카드를 내겠습니까? (0: 카드먹기, 1: 첫번째 카드, 2: ...)"))
    
    if a==0:        #카드 먹기
        cards.append(ob.unopenDeck.pop())           # 언오픈덱에 있는 맨 윗장 먹기
        print("내가 ", cards[-1], "를 먹습니다.")      #디버그용
        #print("내가 한 장을 먹습니다.")
        #ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장

    else:       #카드 내기
        ob.openDeck.append(available[a-1])      # 오픈 덱에 낼 카드 저장
        ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
        print("내가 낸 카드: ", ob.currentCard)
        cards.remove(ob.currentCard)            # 플레이어 카드덱에서 낸 카드는 삭제하기
        print("\n")
        
        
        
def ai_play_game(ob, cards):        #컴퓨터 게임 진행 함수
    
    print("\n\n")
    
    available = []
    for card in cards:
        if (card[0] == ob.currentCard[0] or card[1] == ob.currentCard[1] or card[0] == 'Wild'):     # 낼 수 있는 카드 판
            available.append(card)
    print("놓여진 카드: ", ob.currentCard)
    print("컴퓨터가 낼 수 있는 카드: ", available)
    
    #아직 파이게임으로 구현 못하므로 콘솔창 형태로 제작함
    
    if len(available)==0:        # 카드 먹기
        cards.append(ob.unopenDeck.pop())       # 컴퓨터 카드덱에 언오픈덱 맨 윗장 먹기
        print("컴퓨터가 ", cards[-1], "를 먹습니다.")
        #print("내가 한 장을 먹습니다.")
        #ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장

    else:       #카드 내기
        ob.openDeck.append(available.pop())     # 오픈덱에 컴퓨터가 낼 카드 더하기
        ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
        print("컴퓨터가 낸 카드: ", ob.currentCard)
        cards.remove(ob.currentCard)        # 컴퓨터의 덱에 낸 카드는 삭제시키기
        print("\n")
        
            
        
    '''
        available = []
        for card in self.computer:
            if (card[0] == self.put[-1][0] or card[1] == self.put[-1][1] or card[0] == 'Wild'):
                available.append(card)
        print("놓여진 카드: ", self.put[-1])
        print("컴퓨터가 낼 수 있는 카드: ", available)
        if len(available) > 0:
            self.put.append(available.pop())
            print("컴퓨터가 낸 카드: ", self.put[-1])
            self.computer.remove(self.put[-1])
            
        else:
            self.computer.append(self.card_deck.pop())
            print("컴퓨터가 한 장을 먹습니다.")
        is_myturn = True
        print("\n")
        time.sleep(3)
        
        '''