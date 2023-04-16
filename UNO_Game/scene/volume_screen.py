import pygame
import pygame_gui
import json
from pygame_gui.elements.ui_button import UIButton


pygame.init()

# load json file
with open('display_config.json', 'r') as f:
    config_data = json.load(f)

# extract width and height from the loaded json data
width = config_data['resolution']['width']
height = config_data['resolution']['height']

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("UNO GAME")

manager = pygame_gui.UIManager((width, height))

font = pygame.font.SysFont(None, 100)
uni_font = pygame.font.SysFont(None, 30)

# "Volume" 텍스트 생성
text = font.render("VOLUME", True, (255, 255, 255))
text1 = uni_font.render("Static Sound", True, (255, 255, 255))
text2 = uni_font.render("Background", True, (255, 255, 255))
text3 = uni_font.render("Sound Effect", True, (255, 255, 255))

# 텍스트의 중심 좌표 계산
text_rect = text.get_rect(center=(width//2, height//2 * 0.5))
text1_rect = text1.get_rect(
    center=(width // 2 * 0.5, height // 2))
text2_rect = text2.get_rect(
    center=(width // 2 * 0.5, height // 2 * 1.3))
text3_rect = text3.get_rect(
    center=(width // 2 * 0.5, height // 2 * 1.6))

slider1 = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect(
        (width // 2, height // 2 * 0.9), (width // 4, height // 12)),
    start_value=50.0,
    value_range=(0.0, 100.0, 1.0),
    manager=manager
)

volume_data = {"volume1": slider1.get_current_value()}

slider2 = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect(
        (width // 2, height // 2 * 1.2), (width // 4, height // 12)),
    start_value=50.0,
    value_range=(0.0, 100.0, 1.0),
    manager=manager
)

slider3 = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect(
        (width // 2, height // 2 * 1.5), (width // 4, height // 12)),
    start_value=50.0,
    value_range=(0.0, 100.0, 1.0),
    manager=manager
)

# 나가기버튼 생성
button_rect = pygame.Rect(
    (width // 2 * 0.75, height // 2 * 1.8), (width // 5, height // 15))
reset_button = UIButton(
    relative_rect=button_rect, text='Exit', manager=manager)

# 이벤트 루프
clock = pygame.time.Clock()

run = True
while run:
    delta_time = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("volume.json", "w") as f:
                json.dump(volume_data, f)
            run = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                volume_data["volume1"] = slider1.get_current_value()

        manager.process_events(event)

    manager.update(delta_time)
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
