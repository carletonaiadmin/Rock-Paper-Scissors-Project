# NOTE: Rock is 0, Paper is 1, and Scissors is 2
import random as r
import numpy as np

p1Wins=0
p2Wins=0
p2Vsp1=0.5
winner='none'
p1move=-1
p1Moves=[]
p2Moves=[]
rounds=1
go='yes'

toR = np.zeros((3,3))
toP = np.zeros((3,3))
toS = np.zeros((3,3))

while (go!='q'):
    print('Shoot ', rounds)
    go = input()
    
    if go=='r' or go=='0' : p1move=0
    elif go=='p' or go=='1': p1move=1
    elif go=='s' or go=='2': p1move=2

    if go!='q':

        if (rounds>1):
            p1Last=p1Moves[rounds-2]
            p2Last=p2Moves[rounds-2]
            
            playR=toR[p1Last,p2Last]
            playP=toP[p1Last,p2Last]
            playS=toS[p1Last,p2Last]

            print(toR)
            print(toP)
            print(toS)
            
            # choose AI move
            if playR>playP and playR>playS : p2move=1
            elif playP>playR and playP>playS: p2move=2
            elif playS>playR and playS>playP : p2move=0
            elif playR>playS and playR==playP: p2move=r.choice(1,2)
            elif playR>playP and playR==playS : p2move=r.choice(0,1)
            elif playP>playR and playP==playS : p2move=r.choice(0,2)
            else : p2move=r.randint(0,2)

            # update frequency matrix
            if p1move==0: toR[p1Last,p2Last]=toR[p1Last,p2Last]+1
            elif p1move==1: toP[p1Last,p2Last]=toP[p1Last,p2Last]+1
            elif p1move==2: toS[p1Last,p2Last]=toS[p1Last,p2Last]+1

        else : p2move=r.randint(0,2)
        
        p2move=1
        print(p1move,p2move)

        relThrow=(p1move-p2move)%3
        if relThrow==0: winner='No one Wins!'
        elif relThrow==2:
            winner='AI Wins!'
            p2Wins+=1
        elif relThrow==1:
            winner='You Win!'
            p1Wins+=1
        else: winner='error'
        
        p2Vsp1=p2Wins/rounds

        print(winner)
        p1Moves.append(p1move)
        p2Moves.append(p2move)
        print(p1Moves)
        print(p2Moves)
        rounds+=1
