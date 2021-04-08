import helpers
import hands
import dealer


class Table:
    def __init__(self):

        self.savedata = helpers.helpers.read_file("../resources/save.dat")

        self.player = self.savedata["player"]
        self.table = self.savedata["table"]
        self.round = self.savedata["round"]
        self.cardlist = self.savedata["cardlist"]

        self.pot = self.table[0]
        self.open_cards = self.table[1]

    def add_open(self, cards):
        self.__init__()
        for card in cards:
            self.open_cards.append(card)
        self.save_data()

    def add_private(self):#This will not take any input as dealing private cards is the same each round.
        count = -1
        for players in self.player:
            count += 1
            for card in dealer.dealer.dealcards(2):
                self.__init__()
                self.player[count][0].append(card)
                self.save_data()

    def next(self):
        self.__init__()
        if self.round[1] != len(self.player) - 1:
            self.round[1] += 1
        else:
            self.round[0] += 1
            self.round[1] = 0
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
