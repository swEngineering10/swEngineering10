import pygame
import pygame_gui
import json
from pygame_gui.elements.ui_button import UIButton
from pygame_gui.windows.ui_confirmation_dialog import UIConfirmationDialog


class MainScreen:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = None


basic = MainScreen()
pygame.init()

screen_width = basic.width
screen_height = basic.height

width = 800
height = 600

data = {"resolution": {"width": screen_width, "height": screen_height}}
keyboard_data = {"keyboard": ""}

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("UNO GAME")

manager = pygame_gui.UIManager((screen_width, screen_height))

# 화면 해상도 드롭다운 메뉴 생성
resolution_menu = pygame_gui.elements.UIDropDownMenu(
    options_list=["640x480", "800x600", "1024x768"],
    starting_option="800x600",
    relative_rect=pygame.Rect(
        (basic.width // 2 * 1.1, basic.height // 2 * 0.9), (width // 5, height // 15)),
    manager=manager
)

data["resolution"]["width"] = width
data["resolution"]["height"] = height

# 색약모드 변경 드롭다운 메뉴 생성
color_menu = pygame_gui.elements.UIDropDownMenu(
    options_list=['On', 'Off'],
    starting_option='Off',
    relative_rect=pygame.Rect(
        (basic.width // 2 * 1.1, basic.height // 2 * 1.2), (width // 5, height // 15)),
    manager=manager)

# 키보드 설정 변경 드롭다운 메뉴 생성
keyboard_menu = pygame_gui.elements.UIDropDownMenu(
    options_list=["Up, Down, Left, Right", "W, S, A, D"],
    starting_option="Up, Down, Left, Right",
    relative_rect=pygame.Rect(
        (basic.width // 2 * 1.1, basic.height // 2 * 1.5), (width // 5, height // 15)),
    manager=manager
)

# 리셋버튼 생성
button_rect = pygame.Rect(
    (basic.width // 2 * 0.3, basic.height // 2 * 1.8), (width // 5, height // 15))
reset_button = UIButton(
    relative_rect=button_rect, text='Reset', manager=manager)

# 홈버튼 생성
button_rect2 = pygame.Rect(
    (basic.width // 2 * 1.4, basic.height // 2 * 1.8), (width // 5, height // 15))
home_button = UIButton(
    relative_rect=button_rect2, text='Home', manager=manager)

# 볼륨버튼 생성
button_rect3 = pygame.Rect(
    (basic.width // 2 * 0.85, basic.height // 2 * 1.8), (width // 5, height // 15))
volume_button = UIButton(
    relative_rect=button_rect3, text="Volume", manager=manager)

# 폰트 설정
font = pygame.font.SysFont(None, 100)
uni_font = pygame.font.SysFont(None, 30)

# "SETTING" 텍스트 생성
text = font.render("SETTING", True, (255, 255, 255))
text1 = uni_font.render("Resolution", True, (255, 255, 255))
text2 = uni_font.render("Color Change", True, (255, 255, 255))
text3 = uni_font.render("Keyboard Setting", True, (255, 255, 255))

# 텍스트의 중심 좌표 계산
text_rect = text.get_rect(center=(basic.width//2, basic.height//2 * 0.5))
text1_rect = text1.get_rect(
    center=(basic.width // 2 * 0.5, basic.height // 2))
text2_rect = text2.get_rect(
    center=(basic.width // 2 * 0.5, basic.height // 2 * 1.3))
text3_rect = text3.get_rect(
    center=(basic.width // 2 * 0.5, basic.height // 2 * 1.6))

# 이벤트 루프
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("display_config.json", "w") as file:
                json.dump(data, file, indent=4)
            with open("data.json", "w") as f:
                json.dump(keyboard_data, f)
            run = False
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                # 드롭다운 메뉴에서 선택한 해상도로 화면 크기 변경
                if event.ui_element == resolution_menu:
                    resolution_str = event.text
                    width, height = map(int, resolution_str.split("x"))
                    data["resolution"]["width"] = width
                    data["resolution"]["height"] = height
                    screen = pygame.display.set_mode((width, height))
                    manager = pygame_gui.UIManager((width, height))
                    resolution_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["640x480", "800x600", "1024x768"],
                        starting_option=resolution_str,
                        relative_rect=pygame.Rect(
                            (width // 2 * 1.1, height // 2 * 0.9), (width // 5, height // 15)),
                        manager=manager,
                    )
                    selected_menu1 = resolution_menu.selected_option

                    color_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=['On', 'Off'],
                        starting_option='Off',
                        relative_rect=(
                            (width // 2 * 1.1, height // 2 * 1.2), (width // 5, height // 15)),
                        manager=manager
                    )
                    selected_menu2 = color_menu.selected_option

                    keyboard_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["Up, Down, Left, Right", "W, S, A, D"],
                        starting_option="Up, Down, Left, Right",
                        relative_rect=pygame.Rect(
                            (width // 2 * 1.1, height // 2 * 1.5), (width // 5, height // 15)),
                        manager=manager
                    )
                    selected_menu3 = keyboard_menu.selected_option

                    reset_button = UIButton(
                        relative_rect=pygame.Rect(
                            (width // 2 * 0.3, height // 2 * 1.8), (width // 5, height // 15)),
                        text='Reset',
                        manager=manager
                    )

                    home_button = UIButton(
                        relative_rect=pygame.Rect(
                            (width // 2 * 1.4, height // 2 * 1.8), (width // 5, height // 15)),
                        text='Home',
                        manager=manager
                    )

                    volume_button = UIButton(
                        relative_rect=pygame.Rect(
                            (width // 2 * 0.85, height // 2 * 1.8), (width // 5, height // 15)),
                        text='Volume',
                        manager=manager
                    )

                    # 텍스트의 중심 좌표 계산
                    text_rect = text.get_rect(
                        center=(width//2, height//2 * 0.5))
                    text1_rect = text1.get_rect(
                        center=(width // 2 * 0.5, height // 2))
                    text2_rect = text2.get_rect(
                        center=(width // 2 * 0.5, height // 2 * 1.3))
                    text3_rect = text3.get_rect(
                        center=(width // 2 * 0.5, height // 2 * 1.6))

                elif event.ui_element == color_menu:
                    color_str = event.text
                    color_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=['On', 'Off'],
                        starting_option=color_str,
                        relative_rect=(
                            (width // 2, height // 2 * 1.2), (width // 5, height // 15)),
                        manager=manager
                    )
                    selected_menu2 = color_menu.selected_option

                elif event.ui_element == keyboard_menu:
                    keyboard_str = event.text
                    keyboard_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["Up, Down, Left, Right", "W, S, A, D"],
                        starting_option=keyboard_str,
                        relative_rect=pygame.Rect(
                            (width // 2, height // 2 * 1.5), (width // 5, height // 15)),
                        manager=manager
                    )
                    if event.text == "Up, Down, Left, Right":
                        keyboard_data["keyboard"] = "UDLR"
                    elif event.text == "W, S, A, D":
                        keyboard_data["keyboard"] = "WSAD"
                    selected_menu3 = keyboard_menu.selected_option

            elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == reset_button:
                    width = 800
                    height = 600
                    data["resolution"]["width"] = width
                    data["resolution"]["height"] = height
                    screen = pygame.display.set_mode((width, height))
                    manager = pygame_gui.UIManager((width, height))
                    resolution_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["640x480", "800x600", "1024x768"],
                        starting_option="800x600",
                        relative_rect=pygame.Rect(
                            (width // 2 * 1.1, height // 2 * 0.9), (width // 5, height // 15)),
                        manager=manager,
                    )
                    selected_menu1 = resolution_menu.selected_option

                    color_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=['On', 'Off'],
                        starting_option='Off',
                        relative_rect=(
                            (width // 2 * 1.1, height // 2 * 1.2), (width // 5, height // 15)),
                        manager=manager
                    )
                    selected_menu2 = color_menu.selected_option

                    keyboard_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["Up, Down, Left, Right", "W, S, A, D"],
                        starting_option="Up, Down, Left, Right",
                        relative_rect=pygame.Rect(
                            (width // 2 * 1.1, height // 2 * 1.5), (width // 5, height // 15)),
                        manager=manager
                    )
                    keyboard_data["keyboard"] = "UDLR"
                    selected_menu3 = keyboard_menu.selected_option

                    reset_button = UIButton(
                        relative_rect=pygame.Rect(
                            (width // 2 * 0.3, height // 2 * 1.8), (width // 5, height // 15)),
                        text='Reset',
                        manager=manager
                    )

                    home_button = UIButton(
                        relative_rect=pygame.Rect(
                            (width // 2 * 1.4, height // 2 * 1.8), (width // 5, height // 15)),
                        text='Home',
                        manager=manager
                    )

                    volume_button = UIButton(
                        relative_rect=pygame.Rect(
                            (width // 2 * 0.85, height // 2 * 1.8), (width // 5, height // 15)),
                        text='Volume',
                        manager=manager
                    )

                    # 텍스트의 중심 좌표 계산
                    text_rect = text.get_rect(
                        center=(width//2, height//2 * 0.5))
                    text1_rect = text1.get_rect(
                        center=(width // 2 * 0.5, height // 2))
                    text2_rect = text2.get_rect(
                        center=(width // 2 * 0.5, height // 2 * 1.3))
                    text3_rect = text3.get_rect(
                        center=(width // 2 * 0.5, height // 2 * 1.6))

                elif event.ui_element == volume_button:
                    print("Volume")
        manager.process_events(event)

    manager.update(pygame.time.get_ticks() / 1000)
    screen.fill((0, 0, 0))

    screen.blit(text, text_rect)
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)

    manager.draw_ui(screen)
    pygame.display.update()

print(selected_menu1)
print(selected_menu2)
print(selected_menu3)

pygame.quit()
