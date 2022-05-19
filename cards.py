import random, pygame
from handlers.images_handler import Image



class Card:
    def __init__(self, id, nom, color, state):
        self.pos = [100, 100]
        self.followMouse = False
        self.followMouseOffset = [0, 0]

        # objImageRect = objImage.get_rect()
        # self.img_rect = objImageRect

        self.size = [75, 100]
        self.states = ["deck", "board", "hand"]
        self.id = id
        self.nom = nom
        self.color = color
        self.__state = state #"deck"/"board"/"hand"
        self.dict = dict(zip(["id", "nom", "color", "state"], [self.id, self.nom, self.color, self.__state]))
        self.set_img()

    def view_all(self):
        print(f"size: {self.size}, id: {self.id}, {self.nom}:{self.color}, {self.__state}, pos:{self.pos}, mouse{self.followMouse}, {self.followMouseOffset}")

    def __repr__(self):
        return repr(self.dict)

    def setPosition(self, new_pos):
        self.pos = new_pos

    def rectf(self):
        self.rect = pygame.Rect(self.pos, self.size)#.move(self.pos)
        return self.rect

    def set_img(self):

        if self.color == 'RED':
            self.img = Image(r"images\red.png", self.size, self.pos)
        elif self.color == 'GREEN':
            self.img = Image(r"images\green.png", self.size, self.pos)
        elif self.color == 'BLUE':
            self.img = Image(r"images\blue.png", self.size, self.pos)
        elif self.color == 'YELLOW':
            self.img = Image(r"images\yellow.png", self.size, self.pos)
        else:
            pass



    def change_state(self, new_state):
        if new_state not in self.states:
            error = (f"{new_state} state is not defined.")
            print(error)
        else:
            if self.__state == "hand" or self.__state == "deck":
                self.__state = new_state
            elif self.__state == "board":
                self.__state = self.__state

deck = []
#TODO replace this def into preparing.py
def init_deck():
    id = 0
    color = ["RED", "GREEN", "BLUE", "YELLOW"]
    state = "deck"
    for j in range(2):
        for nom in range(1, 14):
            for c in color:
                deck.append(Card(id=id, nom=nom, color=c, state=state))
                id += 1
    random.shuffle(deck)
    return deck

#test: change_state
#init_deck()
# print(deck[0].get())
#deck[1].change_state("hand")
# print(deck)
# deck[1].change_state("desck")
# print(deck[1].get())
# deck[1].change_state("deck")
# print(deck[1])
# deck[1].change_state("board")
# print(deck[1])
# deck[1].change_state("deck")
# print(deck[1])
# deck[1].change_state("desck")
# print(deck[1])



# for el in field.get(0):
#     x += 50
#     #y += 50
#     el.append(x)
#     el.append(y)
#     print(el)
# print(field.get(0))

