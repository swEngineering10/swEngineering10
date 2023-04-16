import pygame
import pygame_gui
from pygame_gui.elements import UIPanel
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

# 색깔 정의
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

CURRENT_COLOR = "red"

# pygame 초기화
pygame.init()

# 게임 창 생성
pygame.display.set_caption("Pygame GUI Example")
window_surface = pygame.display.set_mode(WINDOW_SIZE)

# UIManager 객체 생성
ui_manager = pygame_gui.UIManager(WINDOW_SIZE)


#레이어 함수
all_sprites = pygame.sprite.LayeredUpdates()

#게임 보드 생성
gameboard = pygame.image.load("./UNO_Game/assets/images/gameboard.png")

background_image = pygame_gui.elements.UIImage(
    relative_rect=pygame.Rect((0, 0), WINDOW_SIZE),
    image_surface=gameboard,
    manager=ui_manager
)

#UNO 버튼 생성
button_rect = pygame.Rect((300, 178), (50, 20))
uno_button = pygame_gui.elements.UIButton(
    relative_rect=button_rect,
    text='UNO',
    manager=ui_manager
)

#색깔 panel 생성
panel_rect = pygame.Rect((300, 158), (20, 20))
color_panel = UIPanel(
    relative_rect=panel_rect,
    manager=ui_manager
    
)

if CURRENT_COLOR == "red":
    color_panel.bg = RED
elif CURRENT_COLOR == "yellow":
    color_panel.bg = YELLOW
elif CURRENT_COLOR == "green":
    color_panel.bg = GREEN
elif CURRENT_COLOR == "blue":
    color_panel.bg = BLUE
                      

all_sprites.add(background_image)
all_sprites.add(uno_button)
all_sprites.add(color_panel)

# 다른 플레이어를 보여줄 보드
playerboard = pygame.image.load("./UNO_Game/assets/images/playerboard.png")
playerinfo = pygame.image.load("./UNO_Game/assets/images/playerinfo.png")

# 내 카드를 보여줄 보드
myboard = pygame.image.load("./UNO_Game/assets/images/myboard.png")

# 카드 이미지
cardback = pygame.image.load("./UNO_Game/assets/images/back.png")
cardback = pygame.transform.scale(cardback, (62, 88))
# 변화된 부분만 업데이트
pygame.display.update()

# MainScreen 인스턴스 생성
main_screen = MainScreen(pygame.Rect((0, 0), WINDOW_SIZE), ui_manager)

# pygame.time.Clock().tick(60) : 화면을 업데이트할 때 사용하는 FPS (Frames Per Second) 값을 설정합니다. 이 코드는 60fps로 설정합니다. 
# 이렇게 설정하면 게임 화면이 초당 60번 업데이트됩니다.
clock = pygame.time.Clock()
# 게임 루프
is_running = True
while is_running:
    # 이전 프레임에서 현재 프레임까지 걸린 시간 (delta time)을 계산합니다. 
    # 이를 통해 애니메이션 및 이동과 같은 모션을 자연스럽게 만들 수 있습니다.
    time_delta = pygame.time.Clock().tick(0) / 1000.0
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN: # 수정 필요.
            if event.key == pygame.K_RETURN:
                if uno_button.check_pressed(event.pos):
                    uno_button.on_click()
  
        #UI manager 업데이트
        ui_manager.process_events(event)
        # 게임 창을 흰색으로 채웁니다. 이전 프레임에서 그려진 모든 것을 지우고 새로운 프레임을 그리기 위해 이 작업을 수행합니다.
        # window_surface.fill(pygame.Color('#FFFFFF'))
        # Pygame GUI에서 관리하는 UI 요소들을 업데이트합니다. 예를 들어, 버튼의 위치나 상태를 업데이트합니다.
        ui_manager.update(time_delta)
        # Pygame GUI에서 관리하는 UI 요소들을 현재 프레임에 그립니다. 이 작업은 Pygame GUI에서 관리하는 모든 요소들을 게임 화면에 그립니다.
        ui_manager.draw_ui(window_surface)
        all_sprites.draw(window_surface)
        # 게임 화면을 업데이트합니다. 이 작업은 이전 화면에서 새 화면으로 모든 변경 사항을 적용하는 것입니다. 이 작업을 수행하지 않으면 게임 화면이 정지되어 있거나, 이전 화면이 그대로 남아 있을 수 있습니다.
        # 이 방식은 화면이 전체적으로 바뀌는 경우에 사용됩니다. 예를 들어, 게임의 한 스테이지에서 다음 스테이지로 넘어갈 때 전체 화면이 교체되는 경우에 사용
        pygame.display.flip()

window_surface.blit(playerboard, (550, 0))
window_surface.blit(myboard, (0, 400)) 
window_surface.blit(gameboard, (0, 0))     
window_surface.blit(cardback, (100, 100))

window_surface.blit(playerinfo, (565, 15))
window_surface.blit(playerinfo, (565, 132))
window_surface.blit(playerinfo, (565, 249))
window_surface.blit(playerinfo, (565, 366))
window_surface.blit(playerinfo, (565, 483)) 

pygame.display.update()

# pygame 종료
pygame.quit()




