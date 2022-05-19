import pygame
from consts import *


class Image:
    def __init__(self, path, start_size=(0,0), start_location=(0,0)):
        self.load = pygame.image.load(path).convert_alpha()
        self.size = start_size
        self.location = start_location
        self.load = pygame.transform.scale(self.load, self.size)
        self.rec = self.load.get_rect()

    def rect(self):
        self.rec.topleft = self.location
        return self.rec


def init_images(display):
    global background
    background = Image(r'images\rumicube_background.jpg', SIZE)
    icon = Image(r"images\ico.jpg", [32, 32])
    global cat
    cat = Image(r'images\cat.gif', (100, 100), [550, 150])
    start_button = Image(r'images\start_button.jpg', (170, 70), [(SIZE[0]-170)/2, 15])
    #red_card = Image(r"images\red_card.jpg", [100, 150], [50, 50])
    cat.load.set_colorkey((255, 255, 255))
    start_button.load.set_colorkey((255, 255, 255))
    display.set_icon(icon.load)
    return cat, background, start_button

