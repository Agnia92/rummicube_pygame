from handlers.event_handler import *
from init_game import *
import init_game

pygame.display.set_caption("Rummicube")
clock = pygame.time.Clock()
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
            running = False # TODO Придумать норм выход из игры. Сейчас закрывает окно и процесс по крестику и Escape.

        # Start a GAME
        if not init_game.game_started and event.type == pygame.MOUSEBUTTONDOWN:
            start(mouse_pos, start_button)
        else:
            if event.type == pygame.KEYDOWN and event.key == 8:
                # TODO откатить одно действие назад (нажатие Backspace)
                pass

            # move and stop
            if event.type == pygame.KEYDOWN:
                if event.scancode in move_direction:
                    start_move(event.scancode)

            if event.type == pygame.KEYUP:
                if event.scancode in move_direction:
                    stop_move(event.scancode)

            if event.type == pygame.MOUSEBUTTONDOWN:
                take(mouse_pos)
# ACTIONS
    if init_game.game_started:
        do_move(cat, background.rect())
        move_card(mouse_pos, pygame.mouse.get_pressed())

# DRAW
    screen.blit(background.load, background.location)
    if not init_game.game_started:
        screen.blit(start_button.load, start_button.location)
    else:
        for curObj in deck:
            screen.blit(curObj.img.load.convert_alpha(), curObj.pos)
        for curObj in player.hand:
            screen.blit(curObj.img.load.convert_alpha(), curObj.pos)

        screen.blit(cat.load, cat.location)
    #screen.blit(deck[3].img.load.convert_alpha(), [250, 350])
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
