import pygame
import pygame_gui


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

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("UNO GAME")

manager = pygame_gui.UIManager((screen_width, screen_height))

# 화면 해상도 드롭다운 메뉴 생성
resolution_menu = pygame_gui.elements.UIDropDownMenu(
    options_list=["640x480", "800x600", "1024x768"],
    starting_option="800x600",
    relative_rect=pygame.Rect(
        (basic.width // 2, basic.height // 2), (200, 50)),
    manager=manager
)

# 색약모드 변경 드롭다운 메뉴 생성
color_menu = pygame_gui.elements.UIDropDownMenu(
    options_list=['On', 'Off'],
    starting_option='On',
    relative_rect=pygame.Rect(
        (basic.width // 2, basic.height // 2 * 1.3), (200, 50)),
    manager=manager)

# 키보드 설정 변경 드롭다운 메뉴 생성
keyboard_menu = pygame_gui.elements.UIDropDownMenu(
    options_list=["Up, Down, Left, Right", "W, S, A, F"],
    starting_option="Up, Down, Left, Right",
    relative_rect=pygame.Rect(
        (basic.width // 2, basic.height // 2 * 1.6), (200, 50)),
    manager=manager
)

# 리셋버튼 생성
button_rect = pygame.Rect(
    (basic.width // 2 - 50, basic.height // 2 * 1.9), (100, 50))
reset_button = pygame_gui.elements.UIButton(
    relative_rect=button_rect, text='Reset', manager=manager)

# 폰트 설정
font = pygame.font.SysFont(None, 100)
uni_font = pygame.font.SysFont(None, 30)

# "SETTING" 텍스트 생성
text = font.render("SETTING", True, (255, 255, 255))
text1 = uni_font.render("Resolution", True, (255, 255, 255))
text2 = uni_font.render("Color Change", True, (255, 255, 255))
text3 = uni_font.render("Keyboard Setting", True, (255, 255, 255))

# 텍스트의 중심 좌표 계산
text_rect = text.get_rect(center=(basic.width//2, basic.height//2 - 100))
text1_rect = text1.get_rect(
    center=(basic.width // 2 - 200, basic.height // 2 + 20))
text2_rect = text2.get_rect(
    center=(basic.width // 2 - 200, basic.height // 2 * 1.3 + 20))
text3_rect = text3.get_rect(
    center=(basic.width // 2 - 200, basic.height // 2 * 1.6 + 20))


# 이벤트 루프
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                # 드롭다운 메뉴에서 선택한 해상도로 화면 크기 변경
                if event.ui_element == resolution_menu:
                    resolution_str = event.text
                    width, height = map(int, resolution_str.split("x"))
                    screen = pygame.display.set_mode((width, height))
                    manager = pygame_gui.UIManager((width, height))
                    resolution_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["640x480", "800x600", "1024x768"],
                        starting_option=resolution_str,
                        relative_rect=pygame.Rect(
                            (width // 2, height // 2), (200, 50)),
                        manager=manager,
                    )
                    color_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=['On', 'Off'],
                        starting_option='On',
                        relative_rect=(
                            (width // 2, height // 2 * 1.3), (200, 50)),
                        manager=manager
                    )
                    keyboard_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["Up, Down, Left, Right", "W, S, A, F"],
                        starting_option="Up, Down, Left, Right",
                        relative_rect=pygame.Rect(
                            (width // 2, height // 2 * 1.6), (200, 50)),
                        manager=manager
                    )
                    reset_button = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(
                            (width // 2 - 50, height // 2 * 1.9), (100, 50)),
                        text='Reset',
                        manager=manager
                    )

                    # 텍스트의 중심 좌표 계산
                    text_rect = text.get_rect(
                        center=(width//2, height//2 - 100))
                    text1_rect = text1.get_rect(
                        center=(width // 2 - 200, height // 2 + 20))
                    text2_rect = text2.get_rect(
                        center=(width // 2 - 200, height // 2 * 1.3 + 20))
                    text3_rect = text3.get_rect(
                        center=(width // 2 - 200, height // 2 * 1.6 + 20))

                elif event.ui_element == color_menu:
                    color_str = event.text
                    color_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=['On', 'Off'],
                        starting_option=color_str,
                        relative_rect=(
                            (width // 2, height // 2 * 1.3), (200, 50)),
                        manager=manager
                    )

                elif event.ui_element == keyboard_menu:
                    keyboard_str = event.text
                    keyboard_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["Up, Down, Left, Right", "W, S, A, F"],
                        starting_option=keyboard_str,
                        relative_rect=pygame.Rect(
                            (width // 2, height // 2 * 1.6), (200, 50)),
                        manager=manager
                    )

            elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == reset_button:
                    width = 800
                    height = 600
                    screen = pygame.display.set_mode((width, height))
                    manager = pygame_gui.UIManager((width, height))
                    resolution_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["640x480", "800x600", "1024x768"],
                        starting_option="800x600",
                        relative_rect=pygame.Rect(
                            (width // 2, height // 2), (200, 50)),
                        manager=manager,
                    )
                    color_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=['On', 'Off'],
                        starting_option='On',
                        relative_rect=(
                            (width // 2, height // 2 * 1.3), (200, 50)),
                        manager=manager
                    )
                    keyboard_menu = pygame_gui.elements.UIDropDownMenu(
                        options_list=["Up, Down, Left, Right", "W, S, A, F"],
                        starting_option="Up, Down, Left, Right",
                        relative_rect=pygame.Rect(
                            (width // 2, height // 2 * 1.6), (200, 50)),
                        manager=manager
                    )
                    reset_button = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(
                            (width // 2 - 50, height // 2 * 1.9), (100, 50)),
                        text='Reset',
                        manager=manager
                    )

                    # 텍스트의 중심 좌표 계산
                    text_rect = text.get_rect(
                        center=(width//2, height//2 - 100))
                    text1_rect = text1.get_rect(
                        center=(width // 2 - 200, height // 2 + 20))
                    text2_rect = text2.get_rect(
                        center=(width // 2 - 200, height // 2 * 1.3 + 20))
                    text3_rect = text3.get_rect(
                        center=(width // 2 - 200, height // 2 * 1.6 + 20))

        manager.process_events(event)

    manager.update(pygame.time.get_ticks() / 1000)
    screen.fill((0, 0, 0))
    manager.draw_ui(screen)
    screen.blit(text, text_rect)
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)
    pygame.display.update()

pygame.quit()
