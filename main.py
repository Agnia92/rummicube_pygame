import pygame, cards
from handlers.images_handler import Image#, background, cat, icon
from handlers.event_handler import *
from consts import *
from cards import *
from player import *

pygame.init()
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Cat's GUN")
background = Image(r'images\rumicube_background.jpg', size)
icon = Image(r"images\ico.jpg", [32, 32])
cat = Image(r'images\cat.gif', (100, 100), [550, 150])
start_button = Image(r'images\start_button.jpg', (170, 70), [(size[0]-170)/2, 15])
#red_card = Image(r"images\red_card.jpg", [100, 150], [50, 50])
cat.load.set_colorkey((255, 255, 255))
start_button.load.set_colorkey((255, 255, 255))
clock = pygame.time.Clock()
pygame.display.set_icon(icon.load)


running = True
x, y = 50, 50
init_deck()
player = Player("Mike")
gameObjects = []
gameObjects.extend(deck)
gameObjects.extend(player.hand)
while running:
    mouse_pos = pygame.mouse.get_pos()
    out = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
            running = False #TODO Придумать норм выход из игры. Сейчас закрывает окно и процесс по крестику и Escape.

        if event.type == pygame.KEYDOWN and event.key == 8:
            #TODO откатить одно действие назад (нажатие Backspace)
            pass

        if event.type == pygame.KEYDOWN:
            if event.scancode in (26,82):
                print("w")
                cat.location[1] -= 5
            if event.key == '1073741905':
                print("s")
                cat.location[1] += 5
            if event.key == '1073741903':
                print("d")
                cat.location[0] += 5
            if event.key == '1073741904':
                print("a")
                cat.location[0] -= 5
            out = True
            if cat.location[0] < 0:
                cat.location[0] = 0
            elif cat.location[1] < 0:
                cat.location[1] = 0
            elif cat.location[0] + cat.size[0] > size[0]:
                cat.location[0] = size[0] - cat.size[0]
            elif cat.location[1] + cat.size[1] > size[1]:
                cat.location[1] = size[1] - cat.size[1]
            else:
                out = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for curObj in gameObjects:
                if curObj.rectf().collidepoint(mouse_pos):
                    curObj.followMouse = True
                    curObj.followMouseOffset = [mouse_pos[0] - curObj.pos[0], mouse_pos[1] - curObj.pos[1]]
                    break
        if event.type == pygame.MOUSEBUTTONUP:
            for curObj in deck:
                if curObj.followMouse == True:
                    curObj.rectf().collidepoint(mouse_pos)
                    curObj.followMouseOffset = [mouse_pos[0] - curObj.pos[0], mouse_pos[1] - curObj.pos[1]]
                    break

        print(event)
    screen.fill(WHITE)


    for curObj in gameObjects:  # в массиве всех созданным нами объектов
        if curObj.followMouse:  ### Если установлен флаг следования за мышкой (объект взят)
            ### получение состояния нажатия всех кнопок мыши
            if pygame.mouse.get_pressed()[0]:  ### проверяем, нажата ли левая кнопка мыши
                newPosX = mouse_pos[0] - curObj.followMouseOffset[0]  ### высчитываем новую позицию с учетом смещения X-координату
                newPosY = mouse_pos[1] - curObj.followMouseOffset[1]  ### Y-координату
                curObj.setPosition([newPosX, newPosY])
            else:  ### если левая кнопка мыши не нажата
                curObj.followMouse = False

    if out == True:
        screen.fill(RED)
    else:
        screen.blit(background.load, background.location)

    for curObj in deck:
        screen.blit(curObj.img.load.convert_alpha(), curObj.pos)
    for curObj in player.hand:
        screen.blit(curObj.img.load.convert_alpha(), curObj.pos)



    #screen.blit(background.load, background.location)
    screen.blit(start_button.load, start_button.location)
    screen.blit(cat.load, cat.location)
    #screen.blit(deck[3].img.load.convert_alpha(), [250, 350])
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
