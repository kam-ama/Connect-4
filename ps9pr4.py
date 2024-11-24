#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """class for an intelligent player"""
    def __init__(self, checker, tiebreak, lookahead):
        """constructure for AI player"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        s = 'Player' + ' ' + self.checker + ' ' + '(' + self.tiebreak + ',' + ' ' + str(self.lookahead) + ')'
        return s
    
    def max_score_column(self, scores):
        """takes a list (scores) containing a score for each column
           of the board, and then returns the index of the column
           with the maximum score
        """
        largest = max(scores)
        indices = []
        for x in range(len(scores)):
            if scores[x] == largest:
                indices += [x]
        if self.tiebreak == 'LEFT':
            return indices[0]
        elif self.tiebreak == 'RIGHT':
            return indices[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(indices)
        
    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer's
           scores for the columns in b
        """
        scores = [0]*b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker):
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                largest = max(opp_scores)
                if largest == 0:
                    scores[col] = 100
                elif largest == 100:
                    scores[col] = 0
                elif largest == 50:
                    scores[col] = 50
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """return the AIPlayer's judgement of its best possible move"""
        scores = self.scores_for(b)
        best = self.max_score_column(scores)
        self.num_moves += 1
        return best