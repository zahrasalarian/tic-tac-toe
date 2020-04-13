"""
Tic Tac Toe Player
"""

import math

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
    x_num = 0
    o_num = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_num += 1
            elif board[i][j] == O:
                o_num += 1
    if x_num > o_num:
        return O
    else:
        return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
    return actions_set
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontally, vertically
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return winner
        elif board[0][i] == board[1][i] == board[2][i]:
            return winner

    # diagonally
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                pass
            else:
                return False
    return True
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
