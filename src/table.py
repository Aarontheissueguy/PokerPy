import helpers
import hands
import dealer

players = 4
buyin = 5

class Table:
    def __init__(self):
        cards_data = helpers.helpers.read_file("../resources/cards.dat")
        self.cards = cards_data
        while True:
            print("trying to load savedata")
            try:
                self.savedata = helpers.helpers.read_file("../resources/save.dat")

                self.player = self.savedata["player"]
                self.table = self.savedata["table"]
                self.round = self.savedata["round"]
                self.cardlist = self.savedata["cardlist"]
                break
            except:
                print("Failed to load savedata. New round was started.")
                dealer.dealer.newround()

        self.pot = self.table[0]
        self.open_cards = self.table[1]

    def add_open(self, cardlist):
        for card in cardlist:
            self.open_cards.append(card)

        self.save_data()

    def save_data(self):
        self.table = [self.pot,self.open_cards]
        value = {
          "player": self.player,
          "table": self.table,
          "round": self.round,
          "cardlist": self.cardlist
        }
        helpers.helpers.save_data("../resources/save.dat", value)

table = Table()
