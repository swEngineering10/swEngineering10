#게임 처음 시작 시 초기화 작업, 다음턴 함수, 규칙에 따라 게임 진행, 게임종료까지 구현한 버전
#우노 작업이랑 타이머 작업은 아직 미구현

import random
from random import randint
import time

# 덱의 가장 위 카드를 뽑아내는 함수 (근데 쓸일이 없었다..)
def pop(cards): 
    return cards[-1]        
        

def init(ob) :      #게임 초기화 함수
    create(ob)      #카드 생성 함수
    random.shuffle(ob.unopenDeck)   # 카드 랜덤하게 섞기
    
    for i in range(ob.numPlayers):  # 카드 7장씩 나누어주기
        for _ in range(7):
            ob.playerList[i].append(ob.unopenDeck.pop())
         
    ob.myTurn = randint(0, ob.numPlayers-1)         # 인간 플레이어 순서 랜덤 지정
    ob.playerTurn = randint(0, ob.numPlayers-1)     # 게임 시작 플레이어 랜덤 지정
    
    print("플레이어는 몇번째 턴?: ", ob.myTurn)
    print("지금 몇번째 순서?: ", ob.playerTurn)
    
    ob.openDeck.append(ob.unopenDeck.pop())  # 미오픈 덱의 첫 번째 카드 오픈 덱으로 이동
    ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장

    
    #처음 시작 카드 관련
    start_card(ob)
    
    #카드 실험용으로 넣은거임!
    #ob.playerList[ob.myTurn].append(("Wild", "Draw4"))


#카드 생성 함수
def create(ob):
    ob.unopenDeck = []   #unopenDeck: 오픈 안한 모든 카드 집합
    colours = ["Red", "Yellow", "Blue", "Green"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Skip", "Riverse", "Draw2", "All_In"]
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


#시작 카드 관련 함수
def start_card(ob):
    while True:
        if ob.currentCard[1] == "Draw4" or ob.currentCard[1] == "Skip" or ob.currentCard[1] == "Swap":
            print("시작카드가", ob.currentCard,"이기 때문에 다시 뽑습니다!")
            ob.openDeck.append(ob.unopenDeck.pop())  # 미오픈 덱의 첫 번째 카드 오픈 덱으로 이동
            ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
            time.sleep(3)
        else:
            break
    if ob.currentCard[1] == "Draw2":
        print("시작카드가", ob.currentCard,"이기 때문에")
        ob.playerList[ob.playerTurn].append(ob.unopenDeck.pop())
        ob.playerList[ob.playerTurn].append(ob.unopenDeck.pop())
        print("시작플레이어인 ",ob.playerTurn,"번째 플레이어가 2장을 먹습니다!")
        set_turn(ob)
    elif ob.currentCard[1] == "Riverse":
        print("시작카드가", ob.currentCard,"이기 때문에 순서 전환됩니다!")
        set_turn(ob)
    elif ob.currentCard[0] == "Wild":
        print("시작카드가", ob.currentCard,"이기 때문에 색깔이 랜덤으로 바뀝니다!")
        ai_color_change(ob)
    time.sleep(3)


#카드 내기 전에 현재 턴의 정보를 출력하는 함수
def print_information(ob, cards):
    print("-----------------------")
    print(ob.turnCount,"번째 게임입니다.")
    print("지금 몇번째 순서?: ", ob.playerTurn)
    ob.available = []          #available: 가지고 있는 덱에서 낼 수 있는 카드 집합
    for card in cards:
        if (card[0] == ob.currentCard[0] or card[1] == ob.currentCard[1] or card[0] == 'Wild'):     #낼 수 있는 카드 판별
            ob.available.append(card)
    print("놓여진 카드: ", ob.currentCard)       #아래부터 나오는 print들은 다 디버그용
    print("낼 수 있는 카드: ", ob.available)
    
#이전 카드가 Draw2카드일 때, 내기 전에 정보를 출력하는 함수
def print_information_Draw2(ob, cards):
    print(ob.turnCount,"번째 게임입니다.")
    print("-----------------------")
    print("지금 몇번째 순서?: ", ob.playerTurn)
    ob.available = []          #available: 가지고 있는 덱에서 낼 수 있는 카드 집합
    for card in cards:
        if (card[1] == 'Draw2'):     #낼 수 있는 카드 판별
            ob.available.append(card)
    print("놓여진 카드: ", ob.currentCard)       #아래부터 나오는 print들은 다 디버그용
    print("낼 수 있는 카드: ", ob.available)


#카드를 한장 먹는 함수
def add_deck(ob, cards):        
    cards.append(ob.unopenDeck.pop())           # 언오픈덱에 있는 맨 윗장 먹기
    #print("내가 ", cards[-1], "를 먹습니다.")      #디버그용
    print(ob.playerTurn,"번째 플레이어가 한 장을 먹습니다.")
    #ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
    ob.playerTurn += ob.playDirection
    over_turn(ob)


#unopenDeck 카드를 섞는 함수
def shuffle_card(ob):
    if len(ob.unopenDeck) == 0:
        print("***남아있는 unopenDeck이 없는 관계로 카드를 섞습니다***")
        ob.unopenDeck = []
        ob.unopenDeck = ob.openDeck
        ob.openDeck = []
        random.shuffle(ob.unopenDeck)   # 카드 랜덤하게 섞기


#플레이어 게임 진행 함수
def play_game(ob, cards):       
    shuffle_card(ob)
    if ob.Draw2Attack == False:     #Draw2 공격 상태가 아니라면
        print_information(ob, cards)
        
        #디버그용. pygame 구현시 마우스 터치 이런형태로 바꿔야함
        a = int(input("몇번째 카드를 내겠습니까? (0: 카드먹기, 1: 첫번째 카드, 2: ...)"))
        
        if a==0:        #카드 먹기
            add_deck(ob, cards)
    
        else:       #카드 내기
            ob.doubleWild = ob.currentCard[0]
            ob.openDeck.append(ob.available[a-1])      # 오픈 덱에 낼 카드 저장
            ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
            print("내가 낸 카드: ", ob.currentCard)
            cards.remove(ob.currentCard)            # 플레이어 카드덱에서 낸 카드는 삭제하기
            is_repeatedcard(ob, cards)
            special_card(ob, cards)
            print("\n")
            set_turn(ob)
            
    elif ob.Draw2Attack == True:    #Draw2 공격 상태라면
        print_information_Draw2(ob, cards)
        
        a = int(input("몇번째 카드를 내겠습니까? (0: 카드먹기, 1: 첫번째 카드, 2: ...)"))
        
        if a==0:
            for i in range(0, ob.Draw2Count*2+1):
                shuffle_card(ob)
                ob.playerList[ob.playerTurn].append(ob.unopenDeck.pop())
            print("방어 실패! ",ob.playerTurn,"번째 플레이어가", ob.Draw2Count * 2,"장을 먹습니다")
            set_turn(ob)
            ob.Draw2Attack = False
            ob.Draw2Count = 0
        else:
            ob.doubleWild = ob.currentCard[0]
            ob.openDeck.append(ob.available[a-1])      # 오픈 덱에 낼 카드 저장
            ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
            print(ob.playerTurn, "번째 플레이어가 낸 카드: ", ob.currentCard)
                        
            cards.remove(ob.currentCard)            # 플레이어 카드덱에서 낸 카드는 삭제하기
            special_card(ob, cards)
            
            print("\n")
            set_turn(ob)
    ob.turnCount += 1
    
    
#중복 카드 검사
def is_repeatedcard(ob, cards):
    ob.available = []
    
    if str(ob.currentCard[1]).isnumeric() == True:
        for card in cards:
            if (card[0] == ob.currentCard[0] and card[1] == ob.currentCard[1]):     #현재 카드와 덱에 숫자, 모양 똑같은 카드가 있다면
                ob.available.append(card)
    else:
        return 0
            
    while(1):      
        if len(ob.available) != 0:
            print("추가로 낼 수 있는 카드", ob.available)
            
            if ob.myTurn == ob.playerTurn:
                a = int(input("중복 카드가 있습니다! 내시겠습니까? (0: 그만 내기, 1: 첫번째 카드, 2: ...)"))
            else:
                a = len(ob.available)
            
            if a == 0:
                break
            else:
                print(a,"번째 카드인 ", ob.available[a-1], "를 냅니다")
                ob.openDeck.append(ob.available[a-1])      # 오픈 덱에 낼 카드 저장
                ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
                ob.available.remove(ob.currentCard)            # 플레이어 카드덱에서 낸 카드는 삭제하기
                cards.remove(ob.currentCard)            # 플레이어 카드덱에서 낸 카드는 삭제하기
        else:
            break
            


#인간 플레이어가 특수카드를 냈을 때 처리        
def special_card(ob, cards):
    if ob.currentCard[0] == "Wild":
        if ob.currentCard[1] == "Color_Change":
            color_change(ob)
            
        if ob.currentCard[1] == "Swap":
            swapedPlayer= int(input("몇번째 플레이어와 카드를 바꾸겠습니까?"))
            ob.playerList[ob.playerTurn], ob.playerList[swapedPlayer] = ob.playerList[swapedPlayer], ob.playerList[ob.playerTurn]
            color_change(ob)
        
        if ob.currentCard[1] == "Draw4":
            print(ob.playerList[ob.myTurn])
            #challenge = 1          #디버그용
            challenge = randint(0, 1)       #ai가 공격할 것인가?
            
            next_turn(ob)   #다음턴 사람은 누구인가?
            
            if challenge==1:        #공격시
                Draw4(ob, cards)
            else:       #도전 자체를 하지 않는다면?
                print("다음턴이 4장을 먹습니다!")
                for i in range(0, 4):
                    shuffle_card(ob)
                    ob.playerList[ob.nextTurn].append(ob.unopenDeck.pop())        #다음턴이 4장 먹음
            ob.playerTurn += ob.playDirection
            over_turn(ob)
            color_change(ob)        
               
    if ob.currentCard[1] == "Draw2":        #다음턴이 두장먹기
        Draw2(ob, cards)
        
    if ob.currentCard[1] == "All_In":       #같은 색상 카드 다 내기
        All_In(ob, cards)
                
        
def Draw4(ob, cards):
    print("다음턴인", ob.nextTurn,"이 도전합니다!")
    is_challenge = 0    #is_challenge: 0이면 공격 실패
    time.sleep(3)
    for i in cards:
        if i[0] == ob.doubleWild:
            is_challenge = 1
            
    if is_challenge==1:     #다음플레이어가 현재턴에게 공격 성공했다면
        print(ob.doubleWild,"와 같은 색상 카드를 가지고 있었습니다! 공격성공!")
        print("현재 플레이어인 ", ob.playerTurn, "이 4장을 먹습니다!")
        for i in range(0, 4):
            shuffle_card(ob)
            ob.playerList[ob.playerTurn].append(ob.unopenDeck.pop())    #본인이 4장 먹음
    else:       #컴퓨터가 나에게 공격 실패했다면
        print(ob.doubleWild,"와 같은 색상 카드가 없었습니다! 공격실패!")
        print("도전에 실패하였습니다! 다음 플레이어인", ob.nextTurn," 이 6장을 먹습니다!")
        for i in range(0, 6):
            shuffle_card(ob)
            ob.playerList[ob.nextTurn].append(ob.unopenDeck.pop())        #다음턴이 6장 먹음
        
        
#다음턴이 두장먹기
def Draw2(ob, cards):
    next_turn(ob)
    ob.playerList[ob.nextTurn].append(ob.unopenDeck.pop())
    print("다음턴인 ",ob.nextTurn,"번째 플레이어에게 Draw2 공격을 합니다!")
    ob.Draw2Attack = True
    ob.Draw2Count += 1
    print("중첩횟수: ", ob.Draw2Count)
    
    #print("다음턴인 ",ob.nextTurn,"번째 플레이어가 2장을 먹습니다")

    
    #순서는 set_turn에서 실행바꿔줌
        
    
#같은 색상 카드 다 내기
def All_In(ob, cards):
    draw_list = []
    for i in cards:
        #print("가진 카드들 리스트: ", i)       #디버그용
        if i[0] == ob.currentCard[0]:
            ob.openDeck.append(i)      # 오픈 덱에 낼 카드 저장
            draw_list.append(i)
            #cards.remove(i)           # 오류나니 쓰지 마
    print("\n",ob.currentCard[0],"인 카드인", draw_list,"를 냅니다")
    ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
    cards = [i for i in cards if i not in draw_list]     # 플레이어 카드덱에서 낸 카드는 삭제하기
        
    
#내가 카드 색깔을 바꾸는 함수  
def color_change(ob):
    newColour = int(input("바꿀 색깔을 1. Blue 2. Red 3.Green 4. Yellow중에서 고르세요."))
    ob.currentCard = (ob.cardColor[newColour-1], " ")
    print(ob.cardColor[newColour-1],"라는 색깔을 선택합니다!")


#ai 게임 진행 함수
def ai_play_game(ob, cards):        
    shuffle_card(ob)
    if ob.Draw2Attack == False:     #Draw2 공격 상태가 아니라면
        print_information(ob, cards)
        if len(ob.available)==0:        # 카드 먹기
            add_deck(ob, cards)
    
        else:       #카드 내기
            ob.doubleWild = ob.currentCard[0]
            ob.openDeck.append(ob.available.pop())     # 오픈덱에 컴퓨터가 낼 카드 더하기
            ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
            print("컴퓨터가 낸 카드: ", ob.currentCard)
            cards.remove(ob.currentCard)        # 컴퓨터의 덱에 낸 카드는 삭제시키기
            is_repeatedcard(ob, cards)
            ai_special_card(ob, cards)
            print("\n")
            set_turn(ob)

    elif ob.Draw2Attack == True:    #Draw2 공격 상태라면
        print_information_Draw2(ob, cards)
        if len(ob.available)==0:
            for i in range(0, ob.Draw2Count*2+1):
                shuffle_card(ob)
                ob.playerList[ob.playerTurn].append(ob.unopenDeck.pop())
            print("방어 실패! ",ob.playerTurn,"번째 플레이어가", ob.Draw2Count * 2,"장을 먹습니다")
            set_turn(ob)
            ob.Draw2Attack = False
            ob.Draw2Count = 0
            
        else:
            ob.doubleWild = ob.currentCard[0]
            ob.openDeck.append(ob.available.pop())     # 오픈덱에 컴퓨터가 낼 카드 더하기
            ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
            print(ob.playerTurn, "번째 플레이어가 낸 카드: ", ob.currentCard)
            cards.remove(ob.currentCard)            # 플레이어 카드덱에서 낸 카드는 삭제하기
            ai_special_card(ob, cards)
            print("\n")
            set_turn(ob)
    ob.turnCount += 1


    time.sleep(3)


#ai가 특수카드를 냈을때 처리
def ai_special_card(ob, cards):
    if ob.currentCard[0] == "Wild":
        if ob.currentCard[1] == "Color_Change":
            ai_color_change(ob)

        if ob.currentCard[1] == "Swap":
            if ob.currentCard[1] == "Swap":
                print("몇번째 플레이어와 카드를 바꾸겠습니까?")
                swapedPlayer= randint(0, ob.numPlayers-1)
                ob.playerList[ob.playerTurn], ob.playerList[swapedPlayer] = ob.playerList[swapedPlayer], ob.playerList[ob.playerTurn]
                ai_color_change(ob)
        
        if ob.currentCard[1] == "Draw4":
            print(ob.playerList[ob.playerTurn])
            #challenge = 1          #디버그용
            
            next_turn(ob)

            if ob.nextTurn != ob.myTurn:      #다음턴이 ai면
                challenge = randint(0, 1)       #ai가 공격할 것인가?
            elif ob.nextTurn == ob.myTurn:    #다음턴이 내차례라면
                challenge = int(input("공격하시겠습니까?(0: 공격하지 않음, 1: 공격함)"))
                
            if challenge==1:        #공격시
                Draw4(ob, cards)
            else:       #도전 자체를 하지 않는다면?
                print("다음턴인 ", ob.nextTurn, "이 4장을 먹습니다!")
                for i in range(0, 4):
                    shuffle_card(ob)
                    ob.playerList[ob.nextTurn].append(ob.unopenDeck.pop())        #다음턴이 4장 먹음
                        
            ai_color_change(ob)        
            ob.playerTurn += ob.playDirection 
            over_turn(ob)
            #ob.playerTurn += ob.playDirection * 2
            
    if ob.currentCard[1] == "Draw2":        #다음턴이 두장먹기
        Draw2(ob, cards)
        
    if ob.currentCard[1] == "All_In":       #같은 색상 카드 다 내기
        All_In(ob, cards)
    
    
#ai가 카드 색깔을 바꾸는 함수
def ai_color_change(ob):    
    print("바꿀 색깔을 1. Blue 2. Red 3.Green 4. Yellow중에서 무작위로 고릅니다.")
    newColour = randint(1, 4)
    ob.currentCard = (ob.cardColor[newColour-1], " ")
    print(ob.cardColor[newColour-1],"라는 색깔을 선택합니다!")



#순서를 정하는 함수
def set_turn(ob): 
    try:
        if ob.currentCard[1] == "Riverse":
            print("순서가 바뀝니다!")
            ob.playDirection *= -1
            ob.playerTurn += ob.playDirection
        elif len(ob.openDeck) == 0:
            ob.playerTurn += ob.playDirection
        elif ob.currentCard[1] == "Skip" or ob.openDeck[1][-1] == "Draw4":
            print("다다음 턴으로 넘어갑니다!")
            ob.playerTurn += ob.playDirection * 2
        else:
            ob.playerTurn += ob.playDirection
    except IndexError:
        ob.playerTurn += ob.playDirection
    over_turn(ob)
        
#다음 playerTurn턴 정할 때 숫자가 넘치지 않나 검사하는 함수
def over_turn(ob):
    if ob.playerTurn == ob.numPlayers + 1:
        ob.playerTurn = 1
    elif ob.playerTurn == ob.numPlayers:
        ob.playerTurn = 0
    elif ob.playerTurn == -1:
        ob.playerTurn = ob.numPlayers - 1
    elif ob.playerTurn == -2:
        ob.playerTurn = ob.numPlayers - 2
        
#다음 nextTurn턴 정할 때 숫자가 넘치지 않나 검사하는 함수(Draw2, Draw4일때만 씀)
def next_turn(ob):
    ob.nextTurn = ob.playerTurn + ob.playDirection
    
    if ob.nextTurn == ob.numPlayers + 1:
         ob.nextTurn = 1
    elif ob.nextTurn == ob.numPlayers:
        ob.nextTurn = 0
    elif ob.nextTurn == -1:
        ob.nextTurn = ob.numPlayers - 1
    elif ob.nextTurn == -2:
        ob.nextTurn = ob.numPlayers - 2
    

        
#게임 종료를 판별하는 함수        
def game_end(ob):
    for i in range(0, ob.numPlayers):
        if len(ob.playerList[i]) == 0:
            print(i,"번째 플레이어가 0장입니다! 게임끝!")
            ob.winner = i
            for i in range(0, ob.numPlayers):
                rank_game(ob, ob.playerList[i])
            print_rank(ob)
            ob.running = False
            
#점수 계산을 해주는 함수            
def rank_game(ob, cards):
    sum = 0
    for card in cards:
        if card[1] == "Draw2" or card[1] == "Riverse" or card[1] == "Skip" or card[1] == "All_In":
            sum += 20
        elif card[1] == "Draw4" or card[1] == "Color_Change":
            sum += 50
        elif card[1] == "Swap":
            sum += 40
        else:
            sum += card[1]
    ob.score.append(sum)
    
#1등을 출력해주는 함수
def print_rank(ob):
    print("winner: ", ob.winner)
    for i in range(0, ob.numPlayers):
        if i != ob.winner:
            print(i,"번째 플레이어: ", ob.score[i])
    
