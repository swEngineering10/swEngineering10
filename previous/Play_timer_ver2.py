# 카드 생성 + 섞기 + 분배 + 낼 수 있는 카드 판독 + 카드 내기 부분까지만 적용한 버전
# 게임시작 클래스 정돈 안함... 타이머 완성되고 게임진행 어느정도 된 뒤에 나중에 할거임..
# 타이머 부분 손봐야하는 버전

import pygame
import random
import time
import signal

'''class Player:
    def __init__(self, name):
        self.deck = []
        self.name = name
        '''
        
class Deck:
    def __init__(self):
        pass
    
    #카드 종류 생성 부분
    def make_card():
        deck = []   #deck: 모든 카드 집합
        colours = ["Red", "Yellow", "Blue", "Green"]
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Skip", "Reverse", "Draw_Two", "All_In"]
        Wild = ["Color_Change", "Draw4", "Swap"]
       
        for colour in colours:      #컬러카드 생성
            for value in values:
                count_card = (colour, value)
                #count_card.append((colour, value))
                #count_card = "{} {}".format(colour, value)
                deck.append(count_card)
                if value!=0:
                    deck.append(count_card)
        for i in Wild:      #와일드카드 생성
            for j in range(4):
                deck.append(('Wild', i))
        return deck
    
    #카드 순서 뒤섞기
    def shuffle_card(deck):
        random.shuffle(deck)
        return deck


class Game:
    #싱글플레이 구현
    def __init__(self):
        
        self.player = []
        self.computer = []
        self.discards = []
        self.deck = Deck()
        #self.p1 = Player('Computer')
        #self.p2 = Player('Me')
        
        #카드 생성+뒤섞기
        self.card_deck = Deck.make_card()
        self.card_deck = Deck.shuffle_card(self.card_deck)
        
    def play_game(self):
        #카드 나눠주기
        for i in range(7):
            self.player.append(self.card_deck.pop())
            self.computer.append(self.card_deck.pop())
        print("플레이어 카드: ", self.player)
        print("컴퓨터 카드: ", self.computer)
        self.put = []       #put_card: 낸 카드
        self.put.append(self.card_deck.pop())
        print("놓여진 카드: ", self.put[-1])
        is_myturn = True    #True: 내 턴이다
        
        print("\n\n")
        
        while True:
            available = []
            try:
            #if is_myturn:
                for card in self.player:
                    if (card[0] == self.put[-1][0] or card[1] == self.put[-1][1] or card[0] == 'Wild'):
                        available.append(card)
                print("놓여진 카드: ", self.put[-1])
                print("내가 낼 수 있는 카드: ", available)
                now_time = time.time()
                is_myturn = False
                
                #아직 파이게임으로 구현 못하므로 콘솔창 형태로 제작함
                
                a = int(input("몇번째 카드를 내겠습니까? (0: 카드먹기, 1: 첫번째 카드, 2: ...)"))
                if a==0:
                    self.player.append(self.card_deck.pop())
                    print("내가 ", self.player[-1], "를 먹습니다.")
                    #print("내가 한 장을 먹습니다.")
                    raise Exception("Next")
                    
                else:
                    self.put.append(available[a-1])
                    print("내가 낸 카드: ", self.put[-1])
                    self.player.remove(self.put[-1])
                    print("\n")
                    
                    
                if time.time() - now_time < 10:
                    print("타임아웃! 컴퓨터 턴으로 넘어갑니다.")
                    is_myturn = False
                    raise Exception("Time out")
                    
                
             
            except:
            #else:
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
            
            
           # print(available)


'''
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()
    
signal.signal(signal.SIGALRM, timeout_handler)

signal.alarm(15)

try:
    your_function()
    # If the function completes before the timeout, cancel the alarm
    signal.alarm(0)
except TimeoutException:
    # If the timeout occurs, handle it by moving on to the next player's turn
    pass

'''






game = Game()
game.play_game()








'''

pygame.init()
font = pygame.font.SysFont("arial", 30, True, True)


# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

button_width = 100
button_height = 50
button_x = (screen_width / 2) - (button_width / 2)
button_y = (screen_height / 2) - (button_height / 2)

'''


'''
#time 부분
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
IsTimeOut = False    #True: 시간오버

#player 관련
player = []         
playing = True      #False: 게임 종료
playing_turn = 0    #0: 시계방향, -1: 반시계방'''


'''
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 현재 시간과 시작 시간의 차이 계산
    current_time = time.time()
    elapsed_time = current_time - start_time

    # 경고 메시지를 표시하는 조건문
    if elapsed_time >= 15:
        debug_text = font.render('Time_Over!', True, (255, 0, 0))
    else:
        debug_text = font.render('Time_Over!', True, (255, 0, 0))
    screen.blit(debug_text, ((screen_width / 2) - (debug_text.get_width() / 2), (screen_height / 2) - (debug_text.get_height() / 2)))
'''

'''
while True:
    if time.time()-start_time < 15: #15초안에 내도록 하기!
        print("시간 초과!")
        break '''

#if IsTimeOut:
    #카드 못내게 함
#else:
    #카드 내게 함


