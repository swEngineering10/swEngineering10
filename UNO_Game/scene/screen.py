#베이스 클래스. 즉 다른 클래스들이 상속받는 클래스
import pygame
import pygame_gui
# screen.py 파일은 실행해도 아무것도 나오지 않습니다. 
# 이 파일은 게임화면을 구현하는 데 필요한 클래스들을 정의하는 모듈일 뿐입니다. 
# 게임을 실행하기 위해서는 screen.py 파일을 import하고, 
# pygame_gui.UIManager 객체와 필요한 BaseScreen 클래스들의 인스턴스를 생성한 뒤, 
# 이를 관리하면서 게임 로직을 실행하는 코드를 작성해야 합니다.
class BaseScreen(pygame_gui.elements.UIWindow):
    def __init__(self, rect, manager, title):
        super().__init__(rect, manager=manager, window_display_title=title)
        self.background_color = pygame.Color('#FFFFFF')
        self.is_visible = False
    
    def show(self):
        self.is_visible = True

    def hide(self):
        self.is_visible = False

    def process_event(self, event):
        pass

    def update(self, time_delta):
        pass

class StartScreen(BaseScreen):
    def __init__(self, rect, manager):
        super().__init__(rect, manager=manager, title='Start Screen')
        # StartScreen에서 필요한 구성 요소들을 추가할 수 있습니다.

class LobbyScreen(BaseScreen):
    def __init__(self, rect, manager):
        super().__init__(rect, manager=manager, title='Lobby Screen')
        # LobbyScreen에서 필요한 구성 요소들을 추가할 수 있습니다.

class MainScreen(BaseScreen):
    def __init__(self, rect, manager):
        super().__init__(rect, manager=manager, title='Main Screen')
        self.background_color = pygame.Color('#FFFFFF')

        label_rect = pygame.Rect((20, 20), (100, 30))
        self.label = pygame_gui.elements.UILabel(
            relative_rect=label_rect, 
            text='Hello World!', 
            manager=manager, 
            container=self
            )
        # MainScreen에서 필요한 구성 요소들을 추가할 수 있습니다.

class SettingScreen(BaseScreen):
    def __init__(self, rect, manager):
        super().__init__(rect, manager=manager, title='Setting Screen')
        # SettingScreen에서 필요한 구성 요소들을 추가할 수 있습니다.
    
