import random
import matplotlib.pyplot as plt


# Game class, has the options, a session tracker and the game state
class Game():
    options = ['rock', 'paper', 'scissors']  # list of choices
    sessions = 0  # tracker for amount of games played
    __state = None  # game state (this attribute is private so it can not be modified by accident)
    session_list = [] 

    def __init__(self):  # constructor that starts the game
        self.__state = True

    def close(self):  # method to close the game
        self.__state = False

    def get_state(self):  # get the current state of the game
        return self.__state

    def get_sessions(self):  # get the amount of times game has ran
        return self.sessions

    def get_session_list(self):  # get the session list
        return self.session_list

    def record(self, human_choice, ai_choice, win): # method to save round data
        round = [human_choice, ai_choice, win]
        self.data.append(round)

    def print_record(self): # method to print all previous round data
        for i in range (0, len(self.data)):
            print("Round # " + str(i+1) + ": " + str(self.data[i][0]) + ", " + str(self.data[i][1]) + ", " + str(self.data[i][2]) + "\n")

    def print_bar_graph(self): # method to print all results of previous rounds as a horiztonal bar graph
        human_wins = 0
        ai_wins = 0
        draws = 0
        result = ''
        for i in range(0, len(self.data)):
            if (self.data[i][2] == "Human"):
                human_wins += 1

            elif (self.data[i][2] == "AI"):
                ai_wins += 1

            else:
                draws += 1
        # HUMAN WINS
        for i in range(0,human_wins):
            result += '#'
        print("Human Wins   :  |" + result)
        result = ''

        # AI WINS
        for i in range(0, ai_wins):
            result += '#'

        print("AI Wins      :  |" + result)
        result = ''

        # DRAWS
        for i in range(0, draws):
            result += '#'

        print("Draws        :  |" + result)
        result = ''

    def save_game(self, file_name): # method to save the game data
        f = open(file_name + '.txt', 'w')

        for i in range(len(self.data)):
            f.writelines( str(self.data[i][0]) + "," + str(self.data[i][1]) + "," + str(self.data[i][2]) + "\n")

        f.close()

    def load_game(self, file_name): # method to load previous game data
        if file_name[len(file_name):len(file_name)-4:-1] == 'txt.':
            pass
        else:
            file_name += '.txt'
        f = open(file_name, 'r')

        self.data = []

        for line in f.readlines():
            line = line[:len(line)-1]
            words = line.split(",")
            self.data.append(words)
            print(line)

        self.sessions = len(self.data)
        f.close()        


# Player class, inherits from Game class
class Player(Game):
    choice = None

    def __init__(self):  # constructor that sets the name to 'Human'
        self.name = 'Human'
        self.win_rate = []
        self.wins = 0

    def set_choice(self):  # get the choice from the human player
        print('Select from rock, paper or scissors')
        self.choice = input('Input your choice: ')

    def get_choice(self):  # get the player's choice
        return self.choice

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

class Frequency(Player):

all_freq = {}

        for i in human_choice:
            if i in human_choice is 0:
                all_freq[0] += 1
                elif i in human_choice is 1:
                    all_freq[1] += 1
                    i = i+1
                    else 
                    all_freq[2] += 1

        

# main function
def main():
    game = Game()  # initialize the Game object
    human = Player()  # initialize the Player object
    ai = AiPlayer()  # initialize the AiPlayer object

    while (game.get_state() == True):  # keep looping if the game state is True
        game.sessions += 1  # track game sessions
        human.set_choice()  # set human choice

        if human.get_choice() not in game.options:  # check the input and break the loop if the input is not what we want
            print('Error 1: Incorrect input')
            break

        ai.set_choice()  # set the ai choice

        print(f'{human.name} selected: {human.get_choice()}') # display the human choice
        print(f'{ai.name} selected: {ai.get_choice()}') # display the ai choice

        # compare the choices and display the winner
        print('------------------------')
        if ai.get_choice() == human.get_choice():
            print('[Draw]')

        elif ai.get_choice() == 'rock' and human.get_choice() == 'scissors':
            print(f'[{ai.name} won]')
            ai.wins += 1

        elif ai.get_choice() == 'paper' and human.get_choice() == 'rock':
            print(f'[{ai.name} won]')
            ai.wins += 1

        elif ai.get_choice() == 'scissors' and human.get_choice() == 'paper':
            print(f'[{ai.name} won]')
            ai.wins += 1

        else:
            print(f'[{human.name} won]')
            human.wins += 1

        ai.win_rate.append(ai.wins / game.get_sessions()) # track the ai win rate
        human.win_rate.append(human.wins / game.get_sessions()) # track the human win rate
        game.session_list.append(game.get_sessions()) # track each game session in a list (used for the matplotlib graph later)

        print('------------------------')
        print(f'Total sessions ran: {game.get_sessions()}')  # display total sessions ran
        print(f'SCORES ---- Humans: {human.wins} AI: {ai.wins}') # display the individual wins
        print(f'AI Win Rate: {ai.get_win_rate()}%') # display the ai win rate 
        print(f'HUMAN Win Rate: {human.get_win_rate()}%') # display the human win rate

        exit_condition = input('Would you like to continue? y/n: ')  # get the exit condition

        if exit_condition not in ['y', 'n']:  # check the input and break the loop if it is not what we want
            print('Error 2: Incorrect input')
            break

        elif exit_condition == 'n':
            plt.plot(game.session_list, ai.win_rate, color='blue')
            plt.plot(game.session_list, human.win_rate, color='green')
            plt.show()
            plt.xlabel('Sessions')
            plt.ylabel('Win Rate')

            game.close()  # close the game

        else:
            continue


# entry point
if __name__ == '__main__':
    main()
