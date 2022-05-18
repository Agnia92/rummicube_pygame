from cards import *

id = 0
#id - is a global variable. it indicates an amount of players in the game
class Player():
    def __init__(self, name):
        global id
        self.name = name
        self.id = id+1
        id += 1
        self.hand = []# list[<int>] ids of cards
        self.init_hand()

    def init_hand(self):
        #global deck
        x = 100
        for i in range(13):
            #print(type(deck[i]))
            self.hand.append(deck[i])
            self.hand[i].pos = [x+self.hand[i].size[0], 700]
            x += self.hand[i].size[0]+10
            self.hand[i].change_state("hand")
            #self.hand[i].rectf().move(100, 100)
            #self.hand[i].pos = self.hand[i].rectf().topleft
            print(self.hand[i].view_all())
            print(deck[i])
        del deck[:13]

    def remove_card_from_hand(self, card):
        print(self.hand)
        self.hand.remove(card)
        card.change_state("board")

        print(self.hand)

#
# p1 = Player("qwer")
# p1.remove_card_from_hand(1)
