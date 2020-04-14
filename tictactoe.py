"""
Tic Tac Toe Player
"""

import math,copy,math

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
    game_player = player(board)

    # making a copy of the board
    board_copy = copy.deepcopy(board)

    action = list(action)
    board_copy[action[0]][action[1]] = game_player

    return board_copy
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontally, vertically
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # diagonally
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    else:
        return None

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

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
        return (-1)
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        x_list = []
        for action in actions(board):
            temp = [action]
            result_board = result(board,action)
            temp.append(min_value(result_board))
            x_list.append(temp)

        max = x_list[0][1]
        ans = x_list[0][0]
        for el in x_list:
            if el[1] > max:
                max = el[1]
                ans = el[0]
        print("max = {}".format(max))
        return ans

    if player(board) == O:
        o_list = []
        for action in actions(board):
            temp = [action]
            result_board = result(board,action)
            temp.append(max_value(result_board))
            o_list.append(temp)

        min = o_list[0][1]
        ans = o_list[0][0]
        print(o_list)
        for el in o_list:
            if el[1] < min:
                min = el[1]
                ans = el[0]

        print("min = {}".format(min))
        return ans
    # raise NotImplementedError

def min_value(board):

    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v

def max_value(board):

    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    return v
