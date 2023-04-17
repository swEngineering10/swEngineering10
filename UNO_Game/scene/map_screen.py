import pygame
import pygame_gui
import json
from pygame_gui.elements.ui_button import UIButton

with open('display_config.json', 'r') as f:
    config_data = json.load(f)

width = config_data['resolution']['width']
height = config_data['resolution']['height']

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("UNO GAME")

manager = pygame_gui.UIManager((width, height))

# 이미지 로드
image1 = pygame.image.load("example1_inactive.png")
image2 = pygame.image.load("example1_active.png")
image3 = pygame.image.load("example2_inactive.png")
image4 = pygame.image.load("example2_active.png")
image5 = pygame.image.load("example3_inactive.png")
image6 = pygame.image.load("example3_active.png")
image7 = pygame.image.load("example4_inactive.png")
image8 = pygame.image.load("example4_active.png")
image9 = pygame.image.load("example5-1.png")
image10 = pygame.image.load("example5-2.png")
image11 = pygame.image.load("example5-3.png")

# 이미지 rect 설정
image_rect = image1.get_rect()
image_rect.center = (width // 2 * 0.3, height // 2 * 0.5)

image_rect2 = image3.get_rect()
image_rect2.center = (width // 2 * 0.75, height // 2 * 1.1)

image_rect3 = image5.get_rect()
image_rect3.center = (width // 2 * 1.15, height // 2 * 0.8)

image_rect4 = image7.get_rect()
image_rect4.center = (width // 2 * 1.6, height // 2 * 1.3)

image_rect5 = image9.get_rect()
image_rect5.center = (width // 2 * 0.6, height // 2 * 0.5)

image_rect6 = image10.get_rect()
image_rect6.center = (width // 2 * 1.05, height // 2 * 1.3)

image_rect7 = image11.get_rect()
image_rect7.center = (width // 2 * 1.5, height // 2 * 0.8)

# 현재 이미지 설정
current_image = image1
current_image2 = image3
current_image3 = image5
current_image4 = image7
current_image5 = image9
current_image6 = image10
current_image7 = image11

button_rect = pygame.Rect(
    (width // 2 * 0.4, height // 2 * 1.7), (width // 5, height // 15))
game_button = UIButton(
    relative_rect=button_rect, text='GAME START', manager=manager)

button_rect = pygame.Rect(
    (width // 2 * 1.2, height // 2 * 1.7), (width // 5, height // 15))
home_button = UIButton(
    relative_rect=button_rect, text='HOME', manager=manager)


while True:
    time_delta = pygame.time.Clock().tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if image_rect.collidepoint(event.pos):
                if current_image == image1:
                    current_image = image2
                else:
                    current_image = image1
            elif image_rect2.collidepoint(event.pos):
                if current_image2 == image3:
                    current_image2 = image4
                else:
                    current_image2 = image3
            elif image_rect3.collidepoint(event.pos):
                if current_image3 == image5:
                    current_image3 = image6
                else:
                    current_image3 = image5
            elif image_rect4.collidepoint(event.pos):
                if current_image4 == image7:
                    current_image4 = image8
                else:
                    current_image4 = image7

    screen.fill((255, 255, 255))

    screen.blit(current_image, image_rect)
    screen.blit(current_image2, image_rect2)
    screen.blit(current_image3, image_rect3)
    screen.blit(current_image4, image_rect4)
    screen.blit(current_image5, image_rect5)
    screen.blit(current_image6, image_rect6)
    screen.blit(current_image7, image_rect7)

    manager.update(time_delta)
    manager.draw_ui(screen)

    pygame.display.update()
