import pygame
from consts import size_board_cell, pos_board, delta


class Background:
    def __init__(self):
        self.board = []
        self.rect = pygame.Rect(pos_board, size_board_cell)
        self.empty = True

    def init_board(self):
        old = self.rect.topleft
        for i in range(4):
            self.board.append([])
            for j in range(1, 17):
                self.board[i].append({"rect": self.rect.copy(), "empty": True})
                self.board[i][j-1].get("rect").topleft = (old[0], old[1])
                old = (old[0] + self.rect.size[0]+delta[0], old[1])
            old = (self.rect.topleft[0], old[1]+self.rect.size[1]+delta[1])

    def magnet(self, card, mouse_pos):
        for line in self.board:
            print(self.board.index(line))
            for item in line:
                rect = item.get("rect")
                if rect.collidepoint(card.old_pos):     # Если карта взята с доски, то ячейка на доске становится пустой
                    item["empty"] = True
                if rect.collidepoint(mouse_pos):    #
                    if item.get("empty"):
                        card.rect.center = rect.center
                        card.setPosition(card.rect.topleft)
                        item["empty"] = False
                        print(card.rect, rect, card.pos, card.size)
                    else:
                        card.pos = card.old_pos
                        print(card.rect, rect)
                        print("pos", card.pos)


b = Background()
b.init_board()
for i in range(4):
    print("Board:", b.board[i])
