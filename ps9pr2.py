#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    def __init__(self, checker):
        """constructure for Player class"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """returns a string representing a Player object"""
        s = 'Player' + ' ' + self.checker
        return s
    
    def opponent_checker(self):
        """returns a one-character string representing the checker
           of the Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns a
           column where the player wants to make the next move
        """
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == False:
                print('Try again!')
            else:
                self.num_moves += 1
                return col