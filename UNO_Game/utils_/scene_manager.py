#화면간의 전환을 처리
import pygame
from states.state import State
from scene.main_screen import MainScreen
from scene.setting_screen import SettingScreen
from scene.lobby_screen import LobbyScreen
from scene.start_screen import StartScreen

class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.scene = None
        

    def set_scene(screen_name):
