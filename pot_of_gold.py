# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 02:45:18 2014

@author: kishor
"""

# There are n-gold pots and two players (A & B)
# Both players exactly know how many coins are there in
# each pot. Player can pick the pot only from the end
# Given that A starts the game, how do you play
# the game A tries to maximize his probability of winning.
# Underlying assumption is that B also tries to play optimally.
POTS = [9,3,4,8]
def pot_of_gold(left, right, player):
    # @left: Left corner of the line of Pot
    # @right: Right corner of the line of Pot
    # @player: Which player is playing the game
    if left > right:
        return 0
    else:
        # Player A tries to maximize his profit in 
        # every attempt
        if player == 'A':
            return max(
                    # Player A picks left Pot                    
                    POTS[left] + pot_of_gold(left+1, right,'B'),
                    # Player A picks right Pot
                    POTS[right] + pot_of_gold(left, right-1, 'B')                    
                    )
        else:
            # Player B tries to minimize what A can gain
            # using available pots
            return min(pot_of_gold(left+1, right, 'A'),
                       pot_of_gold(left, right-1, 'A'))
    
    
if __name__ == '__main__':
     print pot_of_gold(0,3,'A')