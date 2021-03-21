import helpers
import table
import random
player_count = 4

class Dealer:
    def __init__(self):

        cards_data = helpers.helpers.read_file("../resources/cards.dat")
        self.cards = cards_data

        try:
            self.savedata = helpers.helpers.read_file("../resources/save.dat")

            self.player = self.savedata["player"]
            self.table = self.savedata["table"]
            self.round = self.savedata["round"]
            self.cardlist = self.savedata["cardlist"]
        except:
            print("Failed to load savedata. New round was started.")
            self.newround()

    def move(self):
        if self.round[1] == player_count - 1: #player 0 to 3 instead of 1 to 4
            self.round = [self.round[0]+1,0]
            print("here")
        else:
            self.round = [self.round[0],self.round[1]+1]
        self.save_data()

    def newround(self):
        self.player = []
        for p in range(player_count):
            self.player.append([])
        self.table = [0,[]]
        self.round = [0,0] # The total rounds played and the information which players turn it is
        self.cardlist = []
        for color in ["cross","spades","peak","diamonds"]:
            for card in self.cards[color]:
                self.cardlist.append(card)
        self.save_data()

    def dealcards(self,count):
        cards = []
        for num in range(count):
            card = random.choice(self.cardlist)
            cards.append(card)
            self.cardlist.remove(card)

        self.save_data()

        return(cards)



    def save_data(self):
        value = {
          "player": self.player,
          "table": self.table,
          "round": self.round,
          "cardlist": self.cardlist
        }
        helpers.helpers.save_data("../resources/save.dat", value)

dealer = Dealer()
