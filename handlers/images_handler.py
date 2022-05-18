import pygame
from consts import *


class Image:
    def __init__(self, path, start_size=(0,0), start_location=(0,0)):
        self.load = pygame.image.load(path).convert_alpha()
        self.size = start_size
        self.location = start_location
        self.load = pygame.transform.scale(self.load, self.size)

