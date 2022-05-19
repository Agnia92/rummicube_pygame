from consts import *
from init_game import *
import init_game
from cards import deck
from handlers.images_handler import *
#from front import cat
move = STOP
gameObjects = []
gameObjects.extend(deck)
gameObjects.extend(player.hand)


def start_move(direction):
    global move
    if direction in (move_direction[0], move_direction[1]):
        move = UP
    elif direction in (move_direction[2], move_direction[3]):
        move = DOWN
    elif direction in (move_direction[4], move_direction[5]):
        move = LEFT
    elif direction in (move_direction[6], move_direction[7]):
        move = RIGHT
    if move:
        print(f"The cat went {move}.")


def stop_move(direction):
    global move
    if (direction in (move_direction[0], move_direction[1]) and move == UP) \
            or (direction in (move_direction[2], move_direction[3]) and move == DOWN)\
            or (direction in (move_direction[4], move_direction[5]) and move == LEFT)\
            or (direction in (move_direction[6], move_direction[7]) and move == RIGHT):
        move = STOP
        print(f"The cat stopped.")


def do_move(obj, back):
    global move
    if back.contains(obj.rectf()):
        if move == UP:
            print(f"Top-top...")
            obj.location[1] -= 5
        elif move == DOWN:
            print(f"Top-top...")
            obj.location[1] += 5
        elif move == LEFT:
            print(f"Top-top...")
            obj.location[0] -= 5
        elif move == RIGHT:
            print(f"Top-top...")
            obj.location[0] += 5
    else:
        if move == UP:
            obj.location[1] = 0
        elif move == DOWN:
            obj.location[1] = SIZE[1] - obj.size[1]
        elif move == LEFT:
            obj.location[0] = 0
        elif move == RIGHT:
            obj.location[0] = SIZE[0] - obj.size[0]
        move = STOP
        print(f"Dou!")
        print(f"The cat stopped.")


# Mouse_EVENTS
def start(mouse_pos, button):
    # start_button.collidepoint(mouse_pos)
    print(init_game.game_started)
    if button.rectf().collidepoint(mouse_pos):
        init_game.game_started = True


def take(mouse_pos):
    for curObj in gameObjects:
        if curObj.rectf().collidepoint(mouse_pos):
            curObj.old_pos = curObj.pos
            curObj.followMouse = True
            curObj.followMouseOffset = [mouse_pos[0] - curObj.pos[0], mouse_pos[1] - curObj.pos[1]]
            break


def move_card(mouse_pos, mouse_button):
    for curObj in gameObjects:
        if curObj.followMouse: # Знаходимо карту, якщо така є, з прапорцем "слідувати за мишою"
            if mouse_button[0]:
                newposx = mouse_pos[0] - curObj.followMouseOffset[0]
                newposy = mouse_pos[1] - curObj.followMouseOffset[1]
                curObj.setPosition([newposx, newposy])
            else:
                curObj.followMouse = False
                back.magnet(curObj, mouse_pos)




def select_card():
    # TODO select pool of cards
    pass