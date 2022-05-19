import pygame
from consts import size_board_cell


class Background():
    def __init__(self):
        self.board = []
        self.rect = pygame.Rect((0, 0), size_board_cell)

    def init_board(self):
        old = self.rect.topleft
        for i in range(4):
            self.board.append([])
            for j in range(1, 17):
                self.board[i].append(self.rect.copy())
                self.board[i][j-1].topleft = (old[0], old[1])
                old = (old[0] + self.rect.size[0]+10, old[1])
            old = (self.rect.topleft[0], old[1]+self.rect.size[1]+10)

# b = Background()
# b.init_board()
# for i in range(4):
#     print("Board:", b.l[i])
