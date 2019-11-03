import random, json, os
import matplotlib.pyplot as plt


# Game class, has the options, a session tracker and the game state
class Game():
    options = ['rock', 'paper', 'scissors', 'exit']  # list of choices
    sessions = 0  # tracker for amount of games played
    __state = None  # game state (this attribute is private so it can not be modified by accident)
    # game data, to save and retrieve later

    def __init__(self):  # constructor that starts the game
        self.__state = True

    def close(self):  # method to close the game
        self.__state = False

    def get_state(self):  # get the current state of the game
        return self.__state

    def save_game(self, player_data, ai_data, game_data): # method to save the player, ai and game data
        while(True):
            selection = input('Would you like to save the game? (y/n): ') # get the choice
            if selection not in ['y', 'n']: # validate the input
                print('Error 3: Incorrect input')
                continue
            elif selection == 'y':
                filename = input('Please enter the filename: ')
                try: # try/except incase file is not found
                    os.mkdir(f'saves/{filename}') # saves under the "saves" folder
                except FileExistsError as identifier:
                    print(identifier)
                    continue

                with open(f'saves/{filename}/player_data.json', 'w+') as fp:
                    json.dump(player_data, fp) # save player data in json format
                with open(f'saves/{filename}/ai_data.json', 'w+') as fp:
                    json.dump(ai_data, fp) # save ai data in json format
                with open(f'saves/{filename}/game_data.json', 'w+') as fp:
                    json.dump(game_data, fp) # save game data in json format
                break
            else:
                break
            
    def load_game(self): # method to load previous game data
        while(True):
            selection = input('Would you like to load the game? (y/n): ') # get the choice
            if selection not in ['y', 'n']: # validate the input
                print('Error 2: Incorrect input')
                continue
            elif selection == 'y':
                filename = input('Please enter the filename: ')
                try: # try/except incase file is not found
                    with open(f'saves/{filename}/player_data.json', 'r') as fp:
                        player_data = json.load(fp) # read the player data as json
                    with open(f'saves/{filename}/ai_data.json', 'r') as fp:
                        ai_data = json.load(fp) # read the ai data as json
                    with open(f'saves/{filename}/game_data.json', 'r') as fp:
                        game_data = json.load(fp) # read the game data as json
                except FileExistsError as identifier:
                    print(identifier)
                    continue
                
                return (player_data, ai_data, game_data)
            else:
                break


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

class DrawData(Game): # TO:DO class to visualize the data
    def bar_graph(self): 
        pass


# main function
def main():
    game = Game()  # initialize the Game object
    human = Player()  # initialize the Player object
    ai = AiPlayer()  # initialize the AiPlayer object
    data = game.load_game() # ask to load the previous game (load_game() returns a tuple of 3 elements)
    if data != None: # only load if data tuple is non empty
        player_data = data[0] # get the player_data dictionary from tuple
        human.name = player_data['name']
        human.wins = player_data['wins']
        human.win_rate = player_data['win_rate']
        ai_data = data[1] # get the ai_data dictionary from tuple
        ai.name = ai_data['name']
        ai.wins = ai_data['wins']
        ai.win_rate = ai_data['win_rate']
        game_data = data[2] # get the game_data dictionary from tuple
        game.sessions = game_data['sessions']

    while (game.get_state() == True):  # keep looping if the game state is True
        
        human.set_choice()  # set human choice

        if human.choice not in game.options:  # check the input and break the loop if the input is not what we want
            print('Error 1: Incorrect input')
            continue
        
        elif human.choice == 'exit':
            game.close()
            continue

        ai.set_choice()  # set the ai choice

        print(f'{human.name} selected: {human.choice}') # display the human choice
        print(f'{ai.name} selected: {ai.choice}') # display the ai choice

        # compare the choices and display the winner
        print('------------------------')
        if ai.choice == human.choice:
            print('[Draw]')

        elif ai.choice == 'rock' and human.choice == 'scissors':
            print(f'[{ai.name} won]')
            ai.wins += 1

        elif ai.choice == 'paper' and human.choice == 'rock':
            print(f'[{ai.name} won]')
            ai.wins += 1

        elif ai.choice == 'scissors' and human.choice == 'paper':
            print(f'[{ai.name} won]')
            ai.wins += 1

        else:
            print(f'[{human.name} won]')
            human.wins += 1
        print('------------------------')
        
        game.sessions += 1  # track game sessions
        ai.win_rate.append(ai.wins / game.sessions) # track the ai win rate
        human.win_rate.append(human.wins / game.sessions) # track the human win rate

        print(f'SCORES ---- Humans: {human.wins} AI: {ai.wins}') # display the individual wins
        print(f'AI Win Rate: {ai.get_win_rate()}%') # display the ai win rate 
        print(f'HUMAN Win Rate: {human.get_win_rate()}%') # display the human win rate

    player_data = {"name": human.name, "wins": human.wins, "win_rate": human.win_rate}
    ai_data = {"name": ai.name, "wins": ai.wins, "win_rate": ai.win_rate}
    game_data = {"sessions": game.sessions}

    game.save_game(player_data, ai_data, game_data)

# entry point
if __name__ == '__main__':
    main()
