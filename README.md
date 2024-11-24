# Connect-4
Connect Four is a variation of tic-tac-toe played on a 6x7 rectangular board. The game is played by two players, and the goal is to place four checkers in a row vertically, horizontally, or diagonally. The players alternate turns and add one checker to the board at a time. However, because the board stands vertically, a checker cannot be placed in an arbitrary position on the board. Rather, a checker must be inserted at the top of one of the columns, and it “drops down” as far as it can go – until it rests on top of the existing checkers in that column, or (if it is the first checker in that column) until it reaches the bottom row of the column.

Features of the project:

On ps9pr1.py:

    I created a Board class that made a Connect Four board with arbitrary dimensions. In that class are methods that add checkers to the board, removes checkers, and checks if a checker ('X' or 'O') has won the game.

On ps9pr2.py:

    Here I have created a Player superclass that sets the basic methods that identifies the opponent checker and identifies their next move.

On ps9pr3.py:

    This is the Connect Four function that allows the players to play against themselves. There is also a class for a Random AIPlayer, subclass to Player, that makes random moves on the board.

On ps9pr4.py:

    Here I created another subclass to Player: AIPlayer, that makes intelligent moves based on the board. It includes different methods like tiebreak and lookahead that allow it to make better moves against its opponent.
