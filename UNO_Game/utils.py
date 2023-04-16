import engine
import pygame

DARK_GREY = (50,50,50)
MUSTARD = (209,206,25)
BLACK = (0,0,0)

pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 24)

def drawText(screen, t, x, y):
    text = font.render(t, True, MUSTARD, BLACK)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x,y)
    screen.blit(text, text_rectangle)

#IMAGE 파일 변수에 대입


