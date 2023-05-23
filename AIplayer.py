from game_logic import *
from common_function import *
from utility import CardLoad
import pygame

#ai 게임 진행 함수
def ai_play_game(ob, cards):        
    shuffle_card(ob)
                                                                          
    if ob.Draw2Attack == False:     #Draw2 공격 상태가 아니라면
        if ob.currentCard != ("Wild", "Draw4") :
            print_information(ob, cards)
            info(ob)

        if (len(ob.available) == 0) and (ob.currentCard != ("Wild", "Draw4")):        # 낼 수 있는 카드가 없고 draw4 아닐 때 받기
            add_deck(ob, cards)

        # 카드 내기
        elif (len(ob.available) != 0) or (ob.currentCard == ("Wild", "Draw4")):       # 낼 수 있는 카드가 있거나 draw4이면 내기
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

            if ob.currentCard[1] == "Skip" :
                ob.alertType = "skip"
            elif ob.currentCard[1] == "Reverse" :
                ob.alertType = "direction_change"


            if ob.isUnChecked0 :
                # 완료되었을 때 남은 currentCard 이미지 변경
                if (ob.currentCard[1] == "Color_Change") or (ob.currentCard[1] == "Swap") or (ob.currentCard[1] == "Draw4") :
                    ob.open_deck_image_list.append(CardLoad(("Wild", ob.currentCard[1])))
                else :
                    ob.open_deck_image_list.append(CardLoad(ob.currentCard))
                ob.current_card_image = ob.open_deck_image_list[-1]

                # 컴퓨터 플레이어가 카드 낼 때 애니메이션
                ob.current_card_image.set_current_pos([ob.player_deck_image_list[ob.playerTurn-2].player_pos[0], ob.player_deck_image_list[ob.playerTurn-2].player_pos[1]])

                ob.isUnChecked0 = False


    elif ob.Draw2Attack == True:    #Draw2 공격 상태라면
        print_information_Draw2(ob, cards)
        info(ob)
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

            if ob.isUnChecked0 :
                # 완료되었을 때 남은 currentCard 이미지 변경
                if (ob.currentCard[1] == "Color_Change") or (ob.currentCard[1] == "Swap") or (ob.currentCard[1] == "Draw4") :
                    ob.open_deck_image_list.append(CardLoad(("Wild", ob.currentCard[1])))
                else :
                    ob.open_deck_image_list.append(CardLoad(ob.currentCard))
                ob.current_card_image = ob.open_deck_image_list[-1]

                # 컴퓨터 플레이어가 카드 낼 때 애니메이션
                ob.current_card_image.set_current_pos([ob.player_deck_image_list[ob.playerTurn-2].player_pos[0], ob.player_deck_image_list[ob.playerTurn-2].player_pos[1]])

                ob.isUnChecked0 = False

    ob.isAIPlayed = True

    ob.turnCount += 1


#ai가 특수카드를 냈을때 처리
def ai_special_card(ob, cards):
    if ob.currentCard[0] == "Wild":
        if ob.currentCard[1] == "Color_Change":

            ai_color_change(ob)
            ob.playerTurn += ob.playDirection
            over_turn(ob)

        if ob.currentCard[1] == "Swap":

            swapedPlayer= randint(0, ob.numPlayers-1)
            ob.playerList[ob.playerTurn], ob.playerList[swapedPlayer] = ob.playerList[swapedPlayer], ob.playerList[ob.playerTurn]

            # 알림창 띄우기
            if swapedPlayer == ob.playerTurn :
                ob.alerType = "not_swap"
            else :
                ob.alertType = "swap"

            if swapedPlayer == ob.myTurn :      # 스왑한 플레이어가 나면 카드 이미지 갱신
                ob.my_card_list = []
                for i in range(len(ob.playerList[ob.myTurn])) :
                    ob.my_card_list.append(CardLoad(ob.playerList[ob.myTurn][i]))
                    ob.my_card_list[i].swap_card_pop_image(ob.my_card_list)

            ai_color_change(ob)
            ob.playerTurn += ob.playDirection
            over_turn(ob)
        
        # AI가 Draw4를 냈을 때
        if ob.currentCard[1] == "Draw4":
            print(ob.playerList[ob.playerTurn])

            # 아래는 한번만 처리되어야 하는 코드
            if ob.isUnChecked :
                next_turn(ob)   # 다음 턴 계산
                ob.isUnChecked = False

            if ob.nextTurn != ob.myTurn:      #다음턴이 ai면
                challenge = randint(0, 1)       #ai가 공격할 것인가? (0: 공격하지 않음, 1: 공격함)
                if challenge==1:        #공격시
                    Draw4(ob, cards)
                else:       #도전 자체를 하지 않는다면?
                    ob.alertType = "giveup_challenge"    # 다음 플레이어가 4장 받는 알림창 띄우기
                    for i in range(0, 4):
                        shuffle_card(ob)

                        popCard = ob.unopenDeck.pop()
                        ob.playerList[ob.nextTurn].append(popCard)
                                
                    ai_color_change(ob)
                    ob.playerTurn += ob.playDirection
                    over_turn(ob) 
                    ob.playerTurn += ob.playDirection   
                    over_turn(ob)

            elif ob.nextTurn == ob.myTurn:    #다음턴이 내차례라면

                ob.currentPopup = "challenge"   # 챌린지 여부 팝업 띄우기 (입력 받기)
                # 버튼 눌렀을 때만 아래 코드 실행
                if ob.IsChallenge != None :
                    challenge = ob.IsChallenge # 0: 공격하지 않음, 1: 공격함
                
                    if challenge==1:        #공격시
                        Draw4(ob, cards)
                        
                    else:       #도전 자체를 하지 않는다면?
                        ob.alertType = "giveup_challenge"    # 다음 플레이어가 4장 받는 알림창 띄우기
                        for i in range(4):
                            shuffle_card(ob)

                            popCard = ob.unopenDeck.pop()
                            ob.playerList[ob.myTurn].append(popCard)
                            ob.my_card_list.append(CardLoad(popCard))         # 카드 이미지 저장
                            ob.my_card_list[len(ob.my_card_list) - 1].card_pop_image(ob.my_card_list)
                                    
                    ai_color_change(ob)
                    ob.playerTurn += ob.playDirection
                    over_turn(ob) 
                    ob.playerTurn += ob.playDirection   
                    over_turn(ob)
            
    if ob.currentCard[1] == "Draw2":        #다음턴이 두장먹기
        Draw2(ob, cards)
        
    if ob.currentCard[1] == "All_In":       #같은 색상 카드 다 내기
        All_In(ob, cards)
    
    
#ai가 카드 색깔을 바꾸는 함수
def ai_color_change(ob):    
    newColour = randint(1, 4)   # 색깔 무작위로 선택

    # currentCard의 색깔 바꾸기
    if ob.currentCard[1] == "Color_Change" :
        ob.currentCard = (ob.cardColor[newColour-1], "Color_Change")
    elif ob.currentCard[1] == "Draw4" :
        ob.currentCard = (ob.cardColor[newColour-1], "Draw4")
    elif ob.currentCard[1] == "Swap" : 
        ob.currentCard = (ob.cardColor[newColour-1], "Swap")

    ob.colorDelay = 0    
    ob.currentPopup = None
    ob.IsChallenge = None
    ob.isUnChecked = True
    ob.isUnChecked0 = True


def stupid_ai(ob, cards):
    if ob.currentCard == ("Wild", "Draw4") :
        pass
    else :
        ob.doubleWild = ob.currentCard[0]
        ob.openDeck.append(ob.available.pop())     # 오픈덱에 컴퓨터가 낼 카드 더하기
        ob.currentCard = pop(ob.openDeck)        # 오픈 덱의 첫번째 카드 저장
        print("컴퓨터가 낸 카드: ", ob.currentCard)
        cards.remove(ob.currentCard)        # 컴퓨터의 덱에 낸 카드는 삭제시키기
        is_repeatedcard(ob, cards)

    ai_special_card(ob, cards)
    print("\n")

    set_turn(ob)