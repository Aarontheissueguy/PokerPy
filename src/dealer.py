import helpers
import table
import random
player_count = 4

class Dealer:
    def __init__(self):

        cards_data = helpers.helpers.read_file("../resources/cards.dat")
        self.cards = cards_data
        try:
            cardlist_data = helpers.helpers.read_file("../resources/cardlist.dat")
        except:
            cardlist_data = None
        self.cardlist = cardlist_data

        if self.cardlist == None:
            self.cardlist = []
            for color in ["cross","spades","peak","diamonds"]:
                for card in self.cards[color]:
                    self.cardlist.append(card)



    def newround(self):
        helpers.helpers.save_data("../resources/player.dat", None)
        helpers.helpers.save_data("../resources/table.dat", None)
        helpers.helpers.save_data("../resources/cardlist.dat", None)
    def dealcards(self,count):
        cards = []
        for num in range(count):
            card = random.choice(self.cardlist)
            cards.append(card)
            self.cardlist.remove(card)
            print(self.cardlist)
        return(cards)
    def save_data(self):
        helpers.helpers.save_data("../resources/cardlist.dat", self.cardlist)

dealer = Dealer()
dealer.newround()
