from classes.game.game import Game
from classes.decks.game_deck import GameDeck
from classes.cards.card import Card
from classes.auth.user import User
from classes.auth.exceptions import WrongCredentials
import sys
import os

import pickle
import socket
import threading

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# 서버와의 통신을 관리하는 싱글톤 클래스

class Networking:

    # address와 port를 지정하여 소켓 연결을 설정합니다.
    # address: str = socket.gethostname(), port: int = 5499 인자 제외
    def __init__(self):
        self.current_game: Game = Game([], GameDeck())
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.authorized_user = None

        # self._connect(address, port)

    # 서버와 소켓 연결을 설정합니다.
    '''
    def _connect(self, address, port):
        self.sock.connect((address, port))
    '''

    # 사용자 로그인을 처리하는 메서드입니다. username과 password를 송신하여 서버로부터 User 객체와 Game 객체를 받아옵니다.
    # 만약 로그인 정보가 올바르지 않으면 WrongCredentials 예외가 발생합니다.
    '''
    def login(self, username, password) -> User:
        data = {'type': 'login', 'username': username, 'password': password}
        self.sock.sendall(pickle.dumps(data))
        answer = user, game = pickle.loads(self.sock.recv(2048))
        if type(answer) == dict:
            raise WrongCredentials(answer['message'])
        else:
            self.authorized_user = user
            self.current_game = game
            return answer
    '''

    # 사용자 등록을 처리하는 메서드입니다. username과 password를 송신하여 서버로부터 User 객체와 Game 객체를 받아옵니다.
    # 만약 사용자 등록에 실패하면 ValueError 예외가 발생합니다.
    '''
    def register(self, username, password) -> User:
        data = {'type': 'register', 'username': username, 'password': password}
        self.sock.sendall(pickle.dumps(data))
        answer = user, game = pickle.loads(self.sock.recv(2048))
        if type(answer) == dict:
            raise ValueError(answer['message'])
        else:
            self.authorized_user = user
            self.current_game = game
            return answer
    '''

    # 현재 게임 상태를 서버에서 받아옵니다.
    '''
    def fetch(self):
        data = {'type': 'fetch'}
        self.sock.sendall(pickle.dumps(data))
        self.current_game = pickle.loads(self.sock.recv(4096))
    '''

    # 사용자가 카드를 낼 때 호출되는 메서드입니다. card와 ignore를 송신하여 카드를 낼 수 있는지 여부를 서버로부터 받아옵니다.
    '''
    def throw_card(self, card: int | Card, ignore: bool = False) -> bool:
        data = {'type': 'throw', 'card': card, 'ignore': ignore}
        self.sock.sendall(pickle.dumps(data))
        return pickle.loads(self.sock.recv(2048))
    '''

    # 사용자가 카드를 뽑을 때 호출되는 메서드입니다. 서버로부터 뽑을 수 있는지 여부를 받아옵니다.
    '''
    def get_card(self) -> bool:
        data = {'type': 'get_card'}
        self.sock.sendall(pickle.dumps(data))
        return pickle.loads(self.sock.recv(2048))
    '''

    # 사용자의 점수를 증가시키는 메서드입니다. amount를 송신하여 서버로부터 증가한 점수를 받아옵니다.
    '''
    def add_points(self, amount: int = 0) -> bool:
        data = {'type': 'add_points', 'amount': amount}
        self.sock.sendall(pickle.dumps(data))
        return pickle.loads(self.sock.recv(2048))
    '''

    # 사용자가 'Uno'를 외칠 때 호출되는 메서드입니다. 서버로부터 성공 여부를 받아옵니다.
    '''
    def say_uno(self) -> bool:
        data = {'type': 'say_uno'}
        self.sock.sendall(pickle.dumps(data))
        return pickle.loads(self.sock.recv(2048))
    '''

    #  현재 게임에서 authorized_user와 일치하는 User 객체를 반환합니다.
    '''
    def get_user_from_game(self) -> User:
        return [user for user in self.current_game.users if user.id == self.authorized_user.id][0]
    '''

    # 사용자 객체의 인덱스를 반환합니다.
    '''
    def user_id(self, user) -> int:
        return self.current_game.users.index(user)
    '''

    # 현재 사용자의 차례인지 여부를 반환합니다.
    '''
    @property
    def is_our_move(self) -> bool:
        return self.current_game.cur_user_index == self.user_id(self.get_user_from_game())
    '''

    # 클래스 인스턴스가 소멸될 때 호출되는 메서드입니다. 소켓 연결을 닫습니다.
    '''
    def __del__(self):
        self.sock.close()
    '''
