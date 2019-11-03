import random
from game import Game


# Player class, inherits from Game class
class Player(Game):
    choice = None

    def __init__(self):  # constructor that sets the name to 'Human'
        self.name = 'Human'
        self.win_rate = []
        self.wins = 0

    def set_choice(self):  # get the choice from the human player
        print('Select from rock, paper, scissors or exit')
        self.choice = input('Input your choice: ')

    def get_win_rate(self): # get the win rate as a percentage
        return int(self.win_rate[-1]*100) 


# AiPlayer class, inherits from Player class
class AiPlayer(Player):
    def __init__(self):
        self.name = 'AI'  # constructor that sets the name to 'AI'
        self.win_rate = []
        self.wins = 0

    def set_choice(self):  # set the choice for AI
        self.choice = self.options[random.randint(0, 2)]