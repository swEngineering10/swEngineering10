import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("이미지 클릭 예제")

# 이미지 로드
image = pygame.image.load("assets/images/left.png")
image_rect = image.get_rect()

# 이미지 위치 설정
image_x = screen_width // 2 - image_rect.width // 2
image_y = screen_height // 2 - image_rect.height // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 클릭한 위치 확인
            mouse_pos = pygame.mouse.get_pos()
            if image_rect.collidepoint(mouse_pos):
                print("이미지를 클릭했습니다!")

    # 배경 색상 설정
    screen.fill((255, 255, 255))

    # 이미지 그리기
    screen.blit(image, (image_x, image_y))

    # 화면 업데이트
    pygame.display.flip()
