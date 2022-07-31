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
    for row in board:
        count_x += row.count("X")
        count_o += row.count("O")
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
    poss_moves = []
    i = 0
    for row in board:
        j = 0
        for cell in row:
            if cell != "X" and cell != "O":
                poss_moves.append((i, j))
            j += 1
        i += 1
    return poss_moves

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
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
    winner = None
    for row in board:
        if row.count("X") == 3:
            winner = "X"
        elif row.count("O") == 3:
            winner = "O"

    board_transpose = []
    for col in range(3):
        j_to_i = []
        for row in range(3):
            j_to_i.append(board[row][col])
        board_transpose.append(j_to_i)

    for row in board_transpose:
        if row.count("X") == 3:
            winner = "X"
        elif row.count("O") == 3:
            winner = "O"

    board_diag1 = []
    for cell in range(3):
        board_diag1.append(board[cell][cell])
    if board_diag1.count("X") == 3:
        winner = "X"
    elif board_diag1.count("O") == 3:
        winner = "O"

    board_reverse = []
    for row in board:
        row_reverse = row[::-1]
        board_reverse.append(row_reverse)

    board_diag2 = []
    for cell in range(3):
        board_diag2.append(board_reverse[cell][cell])
    if board_diag2.count("X") == 3:
        winner = "X"
    elif board_diag2.count("O") == 3:
        winner = "O"
    
    if winner not in ["X", "O"]:
        winner = None

    return winner

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
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
    v = -float("inf")

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v

def min_value(board):
    v = float("inf")

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == "X":
        
        best_v = -float("inf")
        best_action = None
        
        for action in actions(board):
            v = min_value(result(board, action))
            if v > best_v:
                best_v = v
                best_action = action
        return best_action

    if player(board) == "O":
        
        best_v = float("inf")
        best_action = None
        
        for action in actions(board):
            v = max_value(result(board, action))
            if v < best_v:
                best_v = v
                best_action = action
        return best_action

    raise NotImplementedError
