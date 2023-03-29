import os
import pygame


def load_image(name: str, colorkey: int = None, directory: str = '../assets'):
    fullname = os.path.join(directory, name)
    if not os.path.isfile(fullname):
        raise FileNotFoundError(f"이미지 파일'{fullname}' 을 찾을 수 없습니다.")
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
