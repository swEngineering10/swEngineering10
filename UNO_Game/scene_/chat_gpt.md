import pygame_gui

class BaseScreen(pygame_gui.elements.UIWindow):
def **init**(self, rect, manager, title):
super().**init**(rect, manager=manager, window_display_title=title)
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

class MainScreen(BaseScreen):
def **init**(self, rect, manager):
super().**init**(rect, manager=manager, title='Main Screen') # MainScreen에서 필요한 구성 요소들을 추가할 수 있습니다.

class SettingScreen(BaseScreen):
def **init**(self, rect, manager):
super().**init**(rect, manager=manager, title='Setting Screen') # SettingScreen에서 필요한 구성 요소들을 추가할 수 있습니다.

class LobbyScreen(BaseScreen):
def **init**(self, rect, manager):
super().**init**(rect, manager=manager, title='Lobby Screen') # LobbyScreen에서 필요한 구성 요소들을 추가할 수 있습니다.

class StartScreen(BaseScreen):
def **init**(self, rect, manager):
super().**init**(rect, manager=manager, title='Start Screen') # StartScreen에서 필요한 구성 요소들을 추가할 수 있습니다.

위 코드에서 BaseScreen 클래스는 pygame_gui.elements.UIWindow 클래스를 상속받아서 기본적인 화면을 구현하고, MainScreen, SettingScreen, LobbyScreen, StartScreen 클래스들은 BaseScreen 클래스를 상속받아서 필요한 기능을 추가합니다.

각각의 화면에서는 **init**() 메서드에서 super()를 사용하여 BaseScreen 클래스의 **init**() 메서드를 호출하고, title 매개변수를 통해 화면 제목을 설정합니다. 또한, 필요한 구성 요소들을 추가할 수 있습니다.
