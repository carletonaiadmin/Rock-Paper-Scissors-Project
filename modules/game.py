import os, json


# Game class, has the options, a session tracker and the game state
class Game():
    options = ['rock', 'paper', 'scissors', 'exit']  # list of choices
    sessions = 0  # tracker for amount of games played
    __state = None  # game state (this attribute is private so it can not be modified by accident)
    # game data, to save and retrieve later

    def __init__(self):  # constructor that starts the game
        self.__state = True

    def close(self):  # method to close the game
        '''
        Sets the __state attribute to False
        '''
        self.__state = False

    def get_state(self):  # get the current state of the game
        '''
        Returns the __state attribute
        '''
        return self.__state

    def save_game(self, player_data, ai_data, game_data): # method to save the player, ai and game data
        '''
        Saves all the game info into JSON files under 'saves' sub-directory

        Args:
            player_data: The player data saved as a dictionary {"name": str, "wins": int, "win_rate": []}
            ai_data: The AI data saved as a dictionary {"name": str, "wins": int, "win_rate": []}
            game_data: The game data saved as a dictionary {"sessions": int}
        Returns:
            boolean: Returns True if the function executes, else returns False
        Raises:
            FileExistsError: Raises an exception if a save folder with the same name already exists
        '''
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
                return True
            else:
                return False
            
    def load_game(self): # method to load previous game data
        '''
        Loads all the game info from a folder under 'saves' sub-directory
            
        Returns:
            player_data: The player data saved as a dictionary {"name": str, "wins": int, "win_rate": []}
            ai_data: The AI data saved as a dictionary {"name": str, "wins": int, "win_rate": []}
            game_data: The game data saved as a dictionary {"sessions": int}
            boolean: Returns True if the function executes, else returns False
        Raises:
            FileNotFoundError: Raises an exception if a file is not found
        '''
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
                except FileNotFoundError as identifier:
                    print(identifier)
                    continue
                
                return (player_data, ai_data, game_data, True)
            else:
                return (None, None, None, False)

