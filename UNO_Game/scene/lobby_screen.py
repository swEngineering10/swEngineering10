import pygame
import pygame_gui

pygame.init()

# 화면 크기
screen_width = 800
screen_height = 600

# 화면 생성
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.Surface((screen_width, screen_height))

# 버튼 크기 및 위치
button_count = 5
button_width = 120
button_height = 120
button_spacing = 10 # 버튼의 간격
button_x_pos = screen_width // 2 - ((button_width * (button_count)) + (button_spacing * (button_count - 1))) // 2
button_y_pos = screen_height * 0.6

# 설명 텍스트 내용 및 크기, 위치
text_content = "Computer Player"
font = pygame.font.Font(None, 36)
text = font.render(text_content, True, (255, 255, 255))
text_width, text_height = font.size(text_content)
text_x = screen_width // 2 - text_width // 2
text_y = screen_height // 2 - text_height // 2

# 버튼 생성
button_rects = []
for i in range(button_count):
    # x 좌표가 button_width + button_spacing 만큼 늘어나도록 정사각형 5개 생성
    button_rect = pygame.Rect(button_x_pos + i * (button_width + button_spacing), button_y_pos, button_width, button_height)
    button_rects.append(button_rect)    # button_rects 리스트에 넣기

# 버튼 상태
selected_index = 0
active_index = 1
button_states = ["inactive", "inactive", "inactive", "inactive", "inactive"]
button_states[selected_index] = "selected"
button_states[active_index] = "active"

# 버튼 생성 및 초기화
manager = pygame_gui.UIManager((screen_width, screen_height))
buttons = []
for i in range(button_count):
    button = pygame_gui.elements.UIButton(
        relative_rect=button_rects[i],
        text=str("-"),
        manager=manager
    )
    buttons.append(button)

# 버튼 상태 업데이트 함수
def update_buttons():
    for i, button in enumerate(buttons):
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
        for i, button in enumerate(buttons):
            if event.ui_element == button:
                button_logic(i)
        update_buttons()

# 버튼 로직 함수
def button_logic(button_index):
    global selected_index, active_index
    # 클릭된 버튼이 active 상태일 경우
    if button_states[button_index] == "active":
        if button_index == len(button_rects) - 1:
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
        elif button_index == len(button_rects) - 1:
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

    update_buttons()

    # UIManager 업데이트 및 화면 업데이트
    manager.update(time_delta)
    screen.blit(background, (0, 0))
    screen.blit(text, (text_x, text_y))
    manager.draw_ui(screen)

    pygame.display.update()