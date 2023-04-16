import pygame
import pygame_gui
import sys
import json


class MainScreen:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = None


basic = MainScreen()

# load json file
with open('display_config.json', 'r') as f:
    config_data = json.load(f)

with open("data.json", "r") as f:
    data = json.load(f)  # load data from json file
    keyboard = data["keyboard"]

# extract width and height from the loaded json data
width = config_data['resolution']['width']
height = config_data['resolution']['height']


pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("UNO GAME")

manager = pygame_gui.UIManager((width, height))


def play_mode_function():
    print('Button1 clicked!')


def setting_mode_function():
    print('Button2 clicked!')


def exit_mode_function():
    pygame.quit()
    quit()


button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    width // 2 * 0.8, height // 2, width // 5, height // 15 * 1.1), text='SINGLE PLAY', manager=manager)
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    width // 2 * 0.8, height // 2 * 1.3, width // 5, height // 15 * 1.1), text='SETTING', manager=manager)
button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    width // 2 * 0.8, height // 2 * 1.6, width // 5, height // 15 * 1.1), text='EXIT', manager=manager)

# button dictionary
button_functions = {button1: play_mode_function,
                    button2: setting_mode_function, button3: exit_mode_function}

# 키보드로 버튼 클릭을 제어하는 객체 생성


class KeyboardController:
    def __init__(self, buttons):
        self.buttons = buttons
        self.selected_button_index = 0
        self.buttons[self.selected_button_index]._set_active()

    def handle_event(self, event):
        if keyboard == "UDLR":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_button_index = (
                        self.selected_button_index - 1) % len(self.buttons)
                    self.buttons[self.selected_button_index]._set_active()
                    self.buttons[(self.selected_button_index + 1) %
                                 len(self.buttons)].unselect()
                    self.buttons[(self.selected_button_index + 1) %
                                 len(self.buttons)].enable()
                elif event.key == pygame.K_DOWN:
                    self.selected_button_index = (
                        self.selected_button_index + 1) % len(self.buttons)
                    self.buttons[(self.selected_button_index) %
                                 len(self.buttons)]._set_active()
                    self.buttons[(self.selected_button_index - 1) %
                                 len(self.buttons)].unselect()
                    self.buttons[(self.selected_button_index - 1) %
                                 len(self.buttons)].enable()
                elif event.key == pygame.K_RETURN:
                    clicked_button = self.buttons[self.selected_button_index]
                    if clicked_button in button_functions.keys():
                        button_functions[clicked_button]()
                    elif self.selected_button_index == len(self.buttons) - 1:
                        pygame.quit()
                        sys.exit()
        elif keyboard == "WSAD":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.selected_button_index = (
                        self.selected_button_index - 1) % len(self.buttons)
                    self.buttons[self.selected_button_index]._set_active()
                    self.buttons[(self.selected_button_index + 1) %
                                 len(self.buttons)].unselect()
                    self.buttons[(self.selected_button_index + 1) %
                                 len(self.buttons)].enable()
                elif event.key == pygame.K_s:
                    self.selected_button_index = (
                        self.selected_button_index + 1) % len(self.buttons)
                    self.buttons[(self.selected_button_index) %
                                 len(self.buttons)]._set_active()
                    self.buttons[(self.selected_button_index - 1) %
                                 len(self.buttons)].unselect()
                    self.buttons[(self.selected_button_index - 1) %
                                 len(self.buttons)].enable()
                elif event.key == pygame.K_RETURN:
                    clicked_button = self.buttons[self.selected_button_index]
                    if clicked_button in button_functions.keys():
                        button_functions[clicked_button]()
                    elif self.selected_button_index == len(self.buttons) - 1:
                        pygame.quit()
                        sys.exit()

    def draw(self, surface):
        pass


# 키보드로 제어할 버튼 객체 리스트 생성
keyboard_buttons = [button1, button2, button3]

# 키보드 컨트롤러 객체 생성
keyboard_controller = KeyboardController(keyboard_buttons)

# 폰트 설정
font = pygame.font.SysFont(None, 100)

# "UNO" 텍스트 생성
text = font.render("UNO", True, (255, 255, 255))

# 텍스트의 중심 좌표 계산
text_rect = text.get_rect(center=(width//2, height//2 * 0.6))

# pygame_gui의 UILabel 생성
label = pygame_gui.elements.UILabel(
    relative_rect=text_rect,
    text="",
    manager=manager
)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        manager.process_events(event)
        keyboard_controller.handle_event(event)

        # 마우스 클릭시 버튼 함수 실행
        if event.type == pygame.MOUSEBUTTONUP:
            for button in button_functions.keys():
                if button.rect.collidepoint(event.pos):
                    button_functions[button]()

    manager.update(1 / 60)
    screen.fill((0, 0, 0))
    keyboard_controller.draw(screen)
    screen.blit(text, text_rect)
    manager.draw_ui(screen)
    pygame.display.flip()
