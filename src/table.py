import helpers
import hands

players = 4
buyin = 5

class Table:
    def __init__(self):
        try:
            table_data = helpers.helpers.read_file("../resources/table.dat")
        except:
            table_data = None
        self.table = table_data if table_data != None else [[],["card"]]
        self.pot = self.table[0]
        self.open_cards = self.table[1]
    def add_open(self, cardlist):
        for card in cardlist:
            self.open_cards.append(card)

    def save_data(self):
        helpers.helpers.save_data("../resources/table.dat", [self.pot,self.open_cards])

table = Table()
table.save_data()
