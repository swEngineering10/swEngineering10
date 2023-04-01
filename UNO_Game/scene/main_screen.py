import pygame
import pygame_gui
from screen import MainScreen
# main_screen.py를 실행하면 아무것도 나오지 않습니다. 
# main_screen.py는 단순히 screen.py에서 정의한 MainScreen 클래스를 import하고, 
# 이를 사용하여 게임의 메인 화면을 구성하는 로직을 작성해야 합니다. 
# 예를 들어, pygame.display.set_mode() 함수를 사용하여 게임 창을 생성하고, 
# pygame_gui.UIManager 객체를 생성한 뒤, 
# MainScreen 클래스의 인스턴스를 생성하여 
# UIManager 객체에 등록하는 등의 작업을 수행해야 합니다. 
# 이후 pygame.display.flip() 함수를 호출하여 게임 창을 업데이트하면서 
# MainScreen 클래스에서 정의한 UI 요소들이 화면에 나타납니다.

# 위 코드에서는 먼저 pygame을 초기화하고, 
# pygame.display.set_mode() 함수를 사용하여 게임 창을 생성합니다. 
# 그리고 UIManager 객체를 생성하고, MainScreen 클래스의 인스턴스를 생성하여 
# UIManager 객체에 등록합니다. 그 후 게임 루프를 돌면서 이벤트 처리와 화면 업데이트를 수행하고, 
# 마지막으로 pygame.display.flip() 함수를 호출하여 게임 창을 업데이트합니다.


# 게임 창의 크기를 정의합니다.
WINDOW_SIZE = (800, 600)

# pygame 초기화
pygame.init()

# 게임 창 생성
pygame.display.set_caption("Pygame GUI Example")
window_surface = pygame.display.set_mode(WINDOW_SIZE)

# UIManager 객체 생성
ui_manager = pygame_gui.UIManager(WINDOW_SIZE)

# MainScreen 인스턴스 생성
main_screen = MainScreen(pygame.Rect((0, 0), WINDOW_SIZE), ui_manager)

# 게임 루프
is_running = True
while is_running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        ui_manager.process_events(event)
    
    # 화면 업데이트
    time_delta = pygame.time.Clock().tick(60) / 1000.0
    window_surface.fill(pygame.Color('#FFFFFF'))
    ui_manager.update(time_delta)
    ui_manager.draw_ui(window_surface)
    pygame.display.flip()

# pygame 종료
pygame.quit()




