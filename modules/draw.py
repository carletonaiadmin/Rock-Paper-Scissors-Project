import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from .actors import AiPlayer

class DrawData(AiPlayer): # Inheritance: AiPlayer->Player->Game
    def bar_graph(self,w,d,l):
        plt.figure(1)
        status = ('Win','Draw','Lose')
        statusnumber = (w,d,l)
        y_pos = np.arange(len(status))
        plt.bar(y_pos,statusnumber,align='center',alpha = 0.5)
        plt.xticks(y_pos,status)
        plt.ylabel('Number of Wins, Draws, and Losses')
        plt.title('Statistics')

    def winrate_line_graph(self,WinRatePerson,WinRateAI,GameSession):
        plt.figure(2)
        SessionPlayed = list(range(1,GameSession+1))
        plt.plot(SessionPlayed,WinRateAI,'red')
        plt.plot(SessionPlayed,WinRatePerson,'blue')
        RedPatch = mpatches.Patch(color = 'red',label = 'AI winrate')
        BluePatch = mpatches.Patch(color = 'blue',label = 'Player winrate')
        plt.legend(handles=[RedPatch,BluePatch])
        plt.xlabel("Games Played")
        plt.ylabel("Win Rate")
        plt.title("Win Rates of Human and AI")
        plt.show()
