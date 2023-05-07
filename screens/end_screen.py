import pygame
import pygame.freetype
import pygame_gui
from pygame.surface import Surface
from pygame.event import Event

from client.networking import Networking
from screens.abc_screen import Screen
from utilities.image_utility import load_image
from utilities.text_utility import truncate


class EndScreen(Screen):
    pass