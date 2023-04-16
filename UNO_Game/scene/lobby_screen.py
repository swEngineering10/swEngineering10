import pygame
import pygame_gui
# from screen import LobbyScreen

pygame.init()

# 화면 크기
screen_width = 800
screen_height = 600
WINDOW_SIZE = (screen_width, screen_height)

# 화면 생성
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.Surface((screen_width, screen_height))

# UI manager 생성
manager = pygame_gui.UIManager((screen_width, screen_height))

# LobbyScreen 객체 생성
# lobby_screen = LobbyScreen(pygame.Rect((0, 0), WINDOW_SIZE), manager)

# User Name 텍스트 내용 및 크기, 위치
text_username_content = "User Name"
font_username = pygame.font.Font(None, 50)
text_username = font_username.render(text_username_content, True, (255, 255, 255))
text_username_width, text_username_height = font_username.size(text_username_content)
text_username_x_pos = screen_width // 2 - text_username_width // 2
text_username_y_pos = screen_height * 0.1

# Computer Player 설명 텍스트 내용 및 크기, 위치
text_complayer_content = "Computer Player"
font_complayer = pygame.font.Font(None, 36)
text_complayer = font_complayer.render(text_complayer_content, True, (255, 255, 255))
text_complayer_width, text_complayer_height = font_complayer.size(text_complayer_content)
text_complayer_x_pos = screen_width // 2 - text_complayer_width // 2
text_complayer_y_pos = screen_height * 0.4

# Add Player 버튼 크기 및 위치
add_player_button_count = 5
add_player_button_width = 120
add_player_button_height = 120
add_player_button_spacing = 10 # 버튼의 간격
add_player_button_x_pos = screen_width // 2 - ((add_player_button_width * (add_player_button_count)) + (add_player_button_spacing * (add_player_button_count - 1))) // 2
add_player_button_y_pos = screen_height // 2

# Add Player 버튼 생성
add_player_button_rects = []
for i in range(add_player_button_count):
    button_rect = pygame.Rect(add_player_button_x_pos + i * (add_player_button_width + add_player_button_spacing), add_player_button_y_pos, add_player_button_width, add_player_button_height)
    add_player_button_rects.append(button_rect)

# Add Player 버튼 상태
selected_index = 0
active_index = 1
button_states = ["inactive", "inactive", "inactive", "inactive", "inactive"]
button_states[selected_index] = "selected"
button_states[active_index] = "active"

# 버튼 생성 및 초기화
add_player_buttons = []
for i in range(add_player_button_count):
    button = pygame_gui.elements.UIButton(
        relative_rect=add_player_button_rects[i],
        text=str("-"),
        manager=manager
    )
    add_player_buttons.append(button)

# text entry 생성
username_entry_width = 200
username_entry_height = 50
username_entry_x_pos = screen_width // 2 - username_entry_width // 2
username_entry_y_pos = screen_height * 0.2
username_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((username_entry_x_pos, username_entry_y_pos), (username_entry_width, username_entry_height)),
    manager=manager
)

# Game Start 버튼 생성
start_add_player_button_width = 270
start_add_player_button_height = 70
start_add_player_button_x_pos = screen_width // 2 - start_add_player_button_width // 2
start_add_player_button_y_pos = screen_height * 0.8
start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((start_add_player_button_x_pos, start_add_player_button_y_pos), (start_add_player_button_width, start_add_player_button_height)),
        text=str("Game Start"),
        manager=manager
    )

# 버튼 상태 업데이트 함수
def update_add_player_buttons():
    for i, button in enumerate(add_player_buttons):
        if button_states[i] == "selected":
            button.select()
            button.set_text("computer " + str(i + 1))
        elif button_states[i] == "active":
            button.unselect()       # 이 부분 코드 살짝 꼼수 ㅜㅜ
            button.enable()
            button.set_text("+")
        else:
            button.disable()

# 이벤트 처리 함수
def handle_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    elif event.type == pygame_gui.UI_BUTTON_PRESSED:
        for i, button in enumerate(add_player_buttons):
            if event.ui_element == button:
                add_player_button_logic(i)
                
        update_add_player_buttons()

# 버튼 로직 함수
def add_player_button_logic(button_index):
    global selected_index, active_index
    # 클릭된 버튼이 active 상태일 경우
    if button_states[button_index] == "active":
        if button_index == len(add_player_button_rects) - 1:
            button_states[active_index] = "selected"
            selected_index += 1
        else :
            button_states[active_index] = "selected"
            selected_index += 1
            active_index += 1
            button_states[active_index] = "active"
    # 클릭된 버튼이 inactive 상태일 경우
    elif button_states[button_index] == "inactive":
        pass
    # 클릭된 버튼이 selected 상태일 경우
    else:
        if button_index == 0 :
            pass
        elif button_index != selected_index:
            pass
        elif button_index == len(add_player_button_rects) - 1:
            button_states[selected_index] = "active"
            selected_index -= 1
        else:
            button_states[selected_index] = "active"
            button_states[active_index] = "inactive"
            selected_index -= 1
            active_index -= 1

# main loop
clock = pygame.time.Clock()
while True:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        manager.process_events(event)   # UIManager 이벤트 처리
        handle_event(event)     # 버튼 클릭 이벤트 처리

    update_add_player_buttons()

    # UIManager 업데이트 및 화면 업데이트
    manager.update(time_delta)
    screen.blit(background, (0, 0))
    screen.blit(text_username, (text_username_x_pos, text_username_y_pos))
    screen.blit(text_complayer, (text_complayer_x_pos, text_complayer_y_pos))
    manager.draw_ui(screen)

    pygame.display.update()