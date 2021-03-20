import helpers
colors = ["C","S","P","D"] #cross,spades,peak,diamonds
values = ["j", "q", "k", "a","2","3","4","5","6","7","8","9","10"] #jack, queen, king, ace
diamonds = []
peak = []
spades = []
cross = []

for color in colors:
    if color == "D":
        for val in values:
            diamonds.append(val + color)
for color in colors:
    if color == "P":
        for val in values:
            peak.append(val + color)

for color in colors:
    if color == "S":
        for val in values:
            spades.append(val + color)

for color in colors:
    if color == "C":
        for val in values:
            cross.append(val + color)
print(len(cross)*4)
cards =	{
  "cross": cross,
  "spades": spades,
  "peak": peak,
  "diamonds": diamonds
}

#helpers.helpers.save_data("/home/aaron/Nextcloud/Projekte/GitHub/PokerPy/resources/cards.dat", cards)
print(helpers.helpers.read_file("/home/aaron/Nextcloud/Projekte/GitHub/PokerPy/resources/cards.dat"))
