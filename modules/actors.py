import random, collections
from .game import Game


# Player class, inherits from Game class
class Player(Game):
    choice = None
    history = []

    def __init__(self):  # constructor to initialize Player
        self.name = 'Human' # set the name
        self.win_rate = [] # win rate of all the sessions
        self.wins = 0 # total wins

    def set_choice(self):  # get the choice from the human player
        '''
        Gets the player's choice and assigns it to the 'choice' attribute
        '''
        print('Select from rock, paper, scissors or exit')
        self.choice = input('Input your choice: ')

    def get_win_rate(self): # get the win rate as a percentage
        '''
        Calculates the win rate of the player

        Returns:
            win_rate: Returns the winrate of the last round as a percentage
        '''
        return int(self.win_rate[-1]*100) 

    def get_last_choice(self):
        '''
        Gets the last choice of the player

        Returns:
            last_choice: Returns the the last choice of the player
        '''
        last_choice = self.history[-1]
        return last_choice

    def get_all_choices(self):
        '''
        Gets all of the players choices
        
        Returns:
            last_choice: Returns the last choice of the player
        '''
        last_choice = self.history
        return last_choice

    def frequent_choice(self):
        '''
        Gets the most frequent choice of the player
        
        Returns:
            freq_choice: Returns the most frequent choice of the player
        '''      
        freq_choice = collections.Counter(self.history).most_common()[0][0]
        return freq_choice


# AiPlayer class, inherits from Player class
class AiPlayer(Player):
    def __init__(self): # constructor to initialize AI
        self.name = 'AI'  # set the name
        self.win_rate = [] # win rate of all sessions
        self.wins = 0 # total wins
        self.ties= 0 # total draws

    def set_choice(self):  # set the choice for AI
        '''
        Gets a random choice for the AI and assigns it to the 'choice' attribute
        '''
        self.choice = self.options[random.randint(0, 2)]
