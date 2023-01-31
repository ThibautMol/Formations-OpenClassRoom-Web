"""Jeu du lancé de pièce via une fonction déterminant les probabilités"""

#game A

import random
mise=1000
def play_game_A():
    p = 0.49  # probability of getting tails
    bet = 1  # player's bet in dollars
    mise= 1000
    
    if random.random() < p:
        print("You flipped tails! You win 1 dollar.")
        mise +=1
        return 1  # player wins 1 dollar
        
    else:
        print("You flipped heads. You lose your bet of 1 dollar.")
        mise -=1
        return -1  # player loses 1 dollar
        
    

play_game_A()

while mise < 1000 :
    result = play_game_A()
    if result>0:
        print("You won {} dollar in round {}".format(result,i+1))
    else:
        print("You lost {} dollar in round {}".format(abs(result),i+1))