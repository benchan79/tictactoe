"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    
    # Counts total number of X's and O's on the board
    for row in board:
        count_x += row.count("X")
        count_o += row.count("O")
    
    # If number of X's and O's is the same, then it's player X's turn.
    # Otherwise it is player O's turn.
    if count_x == count_o:
        player = "X"
    else:
        player = "O"
    return player

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    # Actions are added to a set if they're neither an X nor an O
    poss_actions =set()
    i = 0
    for row in board:
        j = 0
        for cell in row:
            if cell != "X" and cell != "O":
                poss_actions.add((i, j))
            j += 1
        i += 1
    return poss_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # Check if attempted action is legal (i.e not in the set of actions(board))
    # If action is legal, make a deepcopy of the board and update new_board with player's action
    # Otherwise raise exception
    if action in actions(board):
        new_board = deepcopy(board)
        i, j = action
        new_board[i][j] = player(board)
    else:
        raise Exception(f"Sorry, move {action} is not a valid move")
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check rows for player who has 3 X's or O's
    # Update code to replace 3 with len(board) to allow for other board sizes
    winner = None
    for row in board:
        if row.count("X") == len(board):
            winner = "X"
        elif row.count("O") == len(board):
            winner = "O"

    # Transpose values into new board to check columns for player who has 3 X's or O's
    # This helps to avoid hardcoding
    board_transpose = []
    for col in range(len(board)):
        j_to_i = []
        for row in range(len(board)):
            j_to_i.append(board[row][col])
        board_transpose.append(j_to_i)

    for row in board_transpose:
        if row.count("X") == len(board):
            winner = "X"
        elif row.count("O") == len(board):
            winner = "O"
    
    # Check first diagonal(upper left to bottom right) for player who has 3 X'a or O's
    # Avoid hardcoding by using board[cell][cell] to check
    board_diag1 = []
    for cell in range(len(board)):
        board_diag1.append(board[cell][cell])
    if board_diag1.count("X") == len(board):
        winner = "X"
    elif board_diag1.count("O") == len(board):
        winner = "O"

    # Reverse every row to check second diagonal(bottom left to upper right)
    # Again this avoids hardcoding by using board[cell][cell] to check
    board_reverse = []
    for row in board:
        row_reverse = row[::-1]
        board_reverse.append(row_reverse)

    board_diag2 = []
    for cell in range(len(board)):
        board_diag2.append(board_reverse[cell][cell])
    if board_diag2.count("X") == len(board):
        winner = "X"
    elif board_diag2.count("O") == len(board):
        winner = "O"
    
    # Return winner = None if there's no winner
    if winner not in ["X", "O"]:
        winner = None

    return winner

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # Check if there's a winner or there're no empty cells left
    # If either condition is True, game has ended and return True
    # 'Flattened' the board using list comprehension to check 2nd condition
    if (winner(board) != None) or (None not in [cell for row in board for cell in row]):
        return True
    else:
        return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

    raise NotImplementedError

def max_value(board):
    # Function to find the max value for given board
    
    # Initiate the value of the board as negative infinity
    v = -float("inf")

    # If game has ended, return its utility value
    if terminal(board):
        return utility(board)

    # Iterate through all possible actions to find the max value
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v

def min_value(board):
    # Function to find the min value for given board
    
    # Initiate the value of the board as positive infinity
    v = float("inf")
    
    # If game has ended, return its utility value
    if terminal(board):
        return utility(board)
    
    # Iterate through all possible actions to find the min value
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    # Find best action for player X
    if player(board) == "X":
        
        best_v = -float("inf")
        best_action = None
        # Go through every possible action
        for action in actions(board):
            # Let v = to value of player O's best action for given board and action
            v = min_value(result(board, action))
            # If player O's v is greater than player X's best_v, assign best_v to v and best_action to that particular action
            if v > best_v:
                best_v = v
                best_action = action
        return best_action

    # Find best action for player O
    if player(board) == "O":
        
        best_v = float("inf")
        best_action = None
        # Go through every possible action        
        for action in actions(board):
            # Let v = to value of player X's best action for given board and action
            v = max_value(result(board, action))
            # If player X's v is smalled than player O's best_v, assign best_v to v and best_action to that particular action
            if v < best_v:
                best_v = v
                best_action = action
        return best_action

    raise NotImplementedError
