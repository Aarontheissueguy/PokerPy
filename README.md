# PokerPy
My attempt of building a well structured holdem game and bot as basis for other Projects.

## How I plan to stucture this project:
I will make the parts of this programs as seperated from one another as possible because I plan to use it for many projects in different ways.
<br>

### The game itself:
<ol>
  <li>hands.py will check wether the card combinations given results in any hands.</li>
  <li>table.py will handle the number of players and which player has what cards.</li>
  <li>dealer.py will take care of things like folding, knocking, playorder, small blind and big blind. It will be the part making everything work together</li>
  <li>main.py will make it easy to controll the whole construct</li>
</ol>
This is just the structure of the dumb and purely luck based game.  
<br>

### The Bot:
My plan is to hand two different values to the bot to define its behavior:
"risk" will define how much risk the bot is willing to take to loose its money, "smartness" will define wether the bot is likely to understand all hands and how far it can think ahead. I will make a variable called "chance" to define how good cards are at any point of the game.
<br>
That is the plan I have in mind. I will start by making the actual poker game.
