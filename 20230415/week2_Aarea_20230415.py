# 지역B 스크립트
import itertools

from class_20230415 import *
from function_20230415 import *

print("A지역에 오신 것을 환영합니다!")
print("나와 1명의 컴퓨터 플레이어와의 대결을 시작합니다!")
print("-----------------------------------------------")

ess = GameInit()   #ess: class 파일 유닛
ess.numPlayers = 2   # 1명의 인간 플레이어 + 1명의 컴퓨터

create(ess)

ess.myTurn = 1         # 인간 플레이어 순서 랜덤 지정
ess.playerTurn = 0      # 우선 0번 플레이어를 컴퓨터로 지정

#컴퓨터부터 카드를 나눠줄거임!
if ess.myTurn != ess.playerTurn:    #컴퓨터에게 가중치만큼 카드 부여하기
    totalcount = 10000
    
    weights_list = [3]*19 + [10]*8 + [3]*19 + [10]*8 + [3]*19 + [10]*8 + [3]*19 + [10]*8 + [10]*12
    result_arr = []
    percent_arr = {}
    #가중치 계산: 668
    #가중치 부여
    
    
    random_num = random.choices(ess.unopenDeck, weights = weights_list, k=7)
    #print(random_num[0])
    for i in range(0,7):
        ess.playerList[ess.playerTurn].append(random_num[i])
        ess.unopenDeck.remove(random_num[i])
    
    ess.playerTurn = 1




######## 검증 부분 ########
'''
#검증용 반복횟수만큼 난수 생성 후 배열에 저장
totalcount = 10000

weights_list = [4]*19 + [10]*8 + [4]*19 + [10]*8 + [4]*19 + [10]*8 + [4]*19 + [10]*8 + [10]*12
result_arr = []
percent_arr = {}
#가중치 계산: 668
#가중치 부여

while len(result_arr) < totalcount:
    random_num = random.choices(ess.unopenDeck, weights = weights_list, k=1)
    result_arr.append(random_num)
    
#ess.playerList[i].append(random_num)

#print("test!!! ", result_arr)
#result_arr.sort()
#result_arr.sort(key = lambda x:x[0])

#result_arr.sort(key = lambda x : x[0])

for lst in map(str, (result_arr)):
    try:
        percent_arr[lst] += 1
    except:
        percent_arr[lst] = 1
        
 
#a = sorted(percent_arr.items(), key = lambda x: x[0])
#sorted(percent_arr.keys())      
#print("test", a)
#a.dict()
#percent_arr.sort(key=lambda percent_arr: percent_arr[0])
        
sum_percent = 0
sum_tech = 0
sum_number = 0 

for key, value in percent_arr.items():
    #if value[1].isdigit()   #기술카드라면
    #숫자별로 나온 개수로 확률 출력
    #print(key, round((value/totalcount)*100, 2))
    #key = key.split(',')
    #key = list(itertools.chain(*key))
    print(key[-3])
    if key[-3].isdigit()==True:
        sum_number += round((value/totalcount)*100, 2)
    else:
        sum_tech += round((value/totalcount)*100, 2)
    
    #전체 확률 합계
    sum_percent += round((value/totalcount)*100, 2)    

print(totalcount,"번 반복시")
print("숫자카드 확률: ", sum_number)
print("기술카드 확률: ", sum_tech)
print("모든 퍼센트 합: ", sum_percent)

# 3 / 668 = 0.00449 >> 19개 * 4 = 76개 >> print시 0.4%
# 10 / 668 = 0.0149 >> 8개 * 4 + 12 = 44개 >> print시 1.4%

'''    
    
    
    

    
#인간한테 카드 그냥 부여
random.shuffle(ess.unopenDeck)
for _ in range(7):
    ess.playerList[ess.playerTurn].append(ess.unopenDeck.pop())    #그냥 부여



#init(ess)      #게임 초기 설정(카드 만들기, 섞기, 분배)
#split_cards(ess)
ess.playerTurn = randint(0, ess.numPlayers-1)     # 게임 시작 플레이어 랜덤 지정
print("플레이어는 몇번째 턴?: ", ess.myTurn)
print("지금 몇번째 순서?: ", ess.playerTurn)

ess.running = True
ess.openDeck.append(ess.unopenDeck.pop())  # 미오픈 덱의 첫 번째 카드 오픈 덱으로 이동
ess.currentCard = pop(ess.openDeck)        # 오픈 덱의 첫번째 카드 저장

#처음 시작 카드 관련
start_card(ess)
ess.smartAi = True
'''
ess.playerList[0].append(('Red', 'Skip'))
ess.playerList[0].append(('Red', 'Skip'))
ess.playerList[0].append(('Red', 'Skip'))
ess.playerList[1].append(('Red', 'Skip'))
ess.playerList[1].append(('Red', 'Skip'))
ess.playerList[1].append(('Red', 'Skip'))
ess.currentCard = ('Red', 2)'''






while ess.running:    
    
    if ess.myTurn == ess.playerTurn :
        play_game(ess, ess.playerList[ess.playerTurn])   #내턴일때
    else:
        ai_play_game(ess, ess.playerList[ess.playerTurn])   #컴퓨터턴일때
        
    game_end(ess)   #결과 출력하고 종료함
