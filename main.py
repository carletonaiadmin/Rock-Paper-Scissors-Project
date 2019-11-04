from modules.game import Game
from modules.actors import Player, AiPlayer
from modules.draw import DrawData

# main function
def main():
    game = Game()  # initialize the Game object
    human = Player()  # initialize the Player object
    ai = AiPlayer()  # initialize the AiPlayer object
    (player_data, ai_data, game_data, loaded) = game.load_game() # ask to load the previous game (load_game() returns a tuple of 4 elements)
    if loaded == True: # only load data if game.load_game() ran succesfully
        human.name = player_data['name']
        human.wins = player_data['wins']
        human.win_rate = player_data['win_rate']
        ai.name = ai_data['name']
        ai.wins = ai_data['wins']
        ai.win_rate = ai_data['win_rate']
        game.sessions = game_data['sessions']
        print('Loaded succesfully')

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
            ai.wins += 1 # increment ai win by 1

        elif ai.choice == 'paper' and human.choice == 'rock':
            print(f'[{ai.name} won]')
            ai.wins += 1 # increment ai win by 1

        elif ai.choice == 'scissors' and human.choice == 'paper':
            print(f'[{ai.name} won]')
            ai.wins += 1 # increment ai win by 1

        else:
            print(f'[{human.name} won]')
            human.wins += 1 # increment player win by 1
        print('------------------------')
        
        game.sessions += 1  # track game sessions
        ai.win_rate.append(ai.wins / game.sessions) # track the ai win rate
        human.win_rate.append(human.wins / game.sessions) # track the human win rate

        print(f'SCORES ---- Humans: {human.wins} AI: {ai.wins}') # display the individual wins
        print(f'AI Win Rate: {ai.get_win_rate()}%') # display the ai win rate 
        print(f'HUMAN Win Rate: {human.get_win_rate()}%') # display the human win rate

    # player, ai and game data is saved in dictionaries for the purpose of saving
    player_data = {"name": human.name, "wins": human.wins, "win_rate": human.win_rate}
    ai_data = {"name": ai.name, "wins": ai.wins, "win_rate": ai.win_rate}
    game_data = {"sessions": game.sessions}

    save_status = game.save_game(player_data, ai_data, game_data) # asks to save the game
    if save_status == True: # print a message if saved succesfully
        print('Saved game succesfully')

# entry point
if __name__ == '__main__':
    main()
