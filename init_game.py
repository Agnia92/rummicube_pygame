from player import Player
from cards import Card, init_deck
import pygame
from consts import *
from handlers.images_handler import init_images
from background import Background

pygame.init()
screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
deck = init_deck()
player = Player("Mike")
cat, background, start_button = init_images(pygame.display)
game_started = False
back = Background()
back.init_board()
