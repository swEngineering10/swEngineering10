# 셋팅에서 쓰이는 모아놓은 클래스

'''
[사용방법]
    헤더에 from setting_class import *
    ess = Setting()
    ess.computer_number = 3 이런식으로 쓰면 됌!
'''



import pygame

class Setting(object):
    def _init__(self):
        self.computer_number = 1        #컴퓨터 수를 넣은 변수
        self.user_name = "user"         #유저 이름을 넣은 변수

    '''
    def __init__(cls, *args):
        #싱글턴 패턴 이용해서 한번만 호출되게끔
        if not cls.computer_number:
            cls._instance = super().__new__(cls)
        return cls._instance
    '''