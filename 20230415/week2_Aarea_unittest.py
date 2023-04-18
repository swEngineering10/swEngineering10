# 지역A 스크립트 검증
import itertools

from class_20230415 import *
from function_20230415 import *

print("A지역에 오신 것을 환영합니다!")
print("확률 검증을 시작하겠습니다!")
print("-----------------------------------------------")

ess = GameInit()   #ess: class 파일 유닛
ess.numPlayers = 2   # 1명의 인간 플레이어 + 1명의 컴퓨터

create(ess)
random_turn(ess)


####### 검증 부분 ########

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

