from game_logic import *
from common_function import ai_color_change

#ai 게임 진행 함수
def ai_play_game(ob, cards):        
    shuffle_card(ob)
    if ob.Draw2Attack == False:     #Draw2 공격 상태가 아니라면
        print_information(ob, cards)
        if len(ob.available)==0:        # 카드 먹기
            add_deck(ob, cards)
    
        else:       #카드 내기
            if ob.smartAi == True:      #지역A의 똑똑한 AI라면?
                for card in ob.available:
                    if (card[1] == 'Skip'):     #낼 수 있는 카드 판별
                        ob.doubleWild = ob.currentCard[0]
                        ob.openDeck.append(card)     # 오픈덱에 컴퓨터가 낼 카드 더하기
                        ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
                        print("컴퓨터가 낸 카드: ", ob.currentCard)
                        cards.remove(ob.currentCard)        # 컴퓨터의 덱에 낸 카드는 삭제시키기
                        print("\n")
                        ob.turnCount += 1
                        return
                stupid_ai(ob, cards)        #skip 카드가 없었다면 평범하게 실행
            else:       #A지역이 아니라면
                stupid_ai(ob, cards)

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


def stupid_ai(ob, cards):
    ob.doubleWild = ob.currentCard[0]
    ob.openDeck.append(ob.available.pop())     # 오픈덱에 컴퓨터가 낼 카드 더하기
    ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
    print("컴퓨터가 낸 카드: ", ob.currentCard)
    cards.remove(ob.currentCard)        # 컴퓨터의 덱에 낸 카드는 삭제시키기
    is_repeatedcard(ob, cards)
    ai_special_card(ob, cards)
    print("\n")
    set_turn(ob)