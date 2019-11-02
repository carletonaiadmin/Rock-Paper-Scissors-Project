import random
import matplotlib.pyplot as plt

# Game class, has the options, a session tracker and the game state
class Game():
    options = ['rock', 'paper', 'scissors']  # list of choices
    sessions = 0  # tracker for amount of games played
    __state = None  # game state (this attribute is private so it can not be modified by accident)
    sessionList = []

    def __init__(self):  # constructor that starts the game
        self.__state = True

    def close(self):  # method to close the game
        self.__state = False

    def get_state(self):  # method to get the current state of the game
        return self.__state

    def get_sessions(self):  # method to return the amount of times game has ran
        return self.sessions

    def get_sessionList(self):
        return self.sessionList
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

    def save_game(self, file_name):
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
        self.winRate = []
        self.wins = 0

    def set_choice(self):  # get the choice from the human player
        print('Select from rock, paper or scissors')
        self.choice = input('Input your choice: ')

    def get_choice(self):  # return the choice
        return self.choice


# AiPlayer class, inherits from Player class
class AiPlayer(Player):
    def __init__(self):
        self.name = 'AI'  # constructor that sets the name to 'AI'
        self.winRate = []
        self.wins = 0

    def set_choice(self):  # set the choice for AI and return it
        self.choice = self.options[random.randint(0, 2)]
        return self.choice


# main function
def main():
    game = Game()  # initialize the Game object
    human = Player()  # initialize the Player object
    ai = AiPlayer()  # initialize the AiPlayer object

    while (game.get_state() == True):  # keep looping if the game state is True
        human.set_choice()  # set human choice

        if human.get_choice() not in game.options:  # check the input and break the loop if the input is not what we want
            print('Error 1: Incorrect input')
            continue

        ai.set_choice()  # set the ai choice

        print(f'{human.name} selected: {human.get_choice()}')
        print(f'{ai.name} selected: {ai.get_choice()}')

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

        game.sessions += 1  # track game sessions


### What is happening here?
        ai.winRate.append(ai.wins / game.get_sessions())
        human.winRate.append(human.wins / game.get_sessions())
        game.sessionList.append(game.get_sessions())
###
        print('------------------------')
        print(f'Total sessions ran: {game.get_sessions()}')  # display total sessions ran
        print(f'SCORES ---- Humans: {human.wins} AI: {ai.wins}')
        print(f'AI WINRATE: {ai.winRate}')
        print(f'HUMAN WINRATE: {human.winRate}')
        print(f'SESSION LIST: {game.sessionList}')

        while(True):
            exit_condition = input('Would you like to continue? y/n: ')  # get the exit condition
            if exit_condition not in ['y', 'n']:  # check the input and break the loop if it is not what we want
                print('Error 2: Incorrect input')
                continue
            else:
                break

        if exit_condition == 'n':
            plt.plot(game.sessionList, ai.winRate, color='blue')
            plt.plot(game.sessionList, human.winRate, color='green')
            plt.show()
            plt.xlabel('Sessions')
            plt.ylabel('Win Rate')
            game.close()  # close the game

        else:
            continue


# entry point
if __name__ == '__main__':
    main()
