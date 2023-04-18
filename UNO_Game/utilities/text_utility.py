import pygame

# center_rect 함수는 surface와 rect 매개 변수를 받습니다. surface는 텍스트가 그려질 pygame surface이며, rect는 텍스트를 중앙에 배치할 사각형 영역입니다. 함수는 rect의 centerx 값을 surface의 중앙값으로 설정합니다.

# text_on_center 함수는 surface, font, text, y 매개 변수를 받습니다. surface는 텍스트가 그려질 pygame surface이며, font는 텍스트에 사용될 pygame freetype font입니다. text는 그려질 텍스트이며, y는 텍스트가 그려질 y 좌표입니다. 함수는 텍스트를 font와 text 매개 변수로 렌더링한 후, 중앙에 위치하도록 text_rect를 조정하고 surface에 텍스트를 렌더링합니다.

# truncate 함수는 text, max_len, ending 매개 변수를 받습니다. text는 자를 텍스트입니다. max_len은 반환할 텍스트의 최대 길이이며, 기본값은 7입니다. ending은 텍스트가 최대 길이보다 길 때 끝에 추가할 문자열이며, 기본값은 '...'입니다. 함수는 텍스트가 최대 길이보다 길 경우, ending을 붙인 후 max_len에 맞게 자른 텍스트를 반환합니다. 그렇지 않으면 원래의 텍스트를 반환합니다.

def center_rect(surface, rect: pygame.rect.Rect):
    rect.centerx = surface.get_width() // 2


def text_on_center(surface: pygame.surface.Surface, font: pygame.freetype.Font, text: str, y: int):
    text_rect = font.get_rect(text)
    center_rect(surface, text_rect)
    text_rect.centery = y
    font.render_to(surface, text_rect, text)


def truncate(text: str, max_len: int = 7, ending: str = '...') -> str:
    if len(text) > max_len:
        return text[:max_len - len(ending)] + ending
    else:
        return text
