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
    if(board == initial_state()):
        return X
    countx = 0
    counto = 0
    for i in range(3):
        for j in range(3):
            if(board[i][j] == X):
                countx += 1
            elif(board[i][j] == O):
                counto += 1
    if(countx > counto):
        return O
    elif(countx < counto):
        return X
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                actions.add((i, j)) 
    return actions        
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Invalid action")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if(board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY):
            return board[i][0]
    for j in range(3):
        if(board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY):
            return board[0][j]
    if(board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY):
        return board[0][0]
    if(board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY):
        return board[0][2]
    return None             
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != None):
        return True
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(terminal(board) == True):
        if(winner(board) == X):
            return 1
        elif(winner(board) == O):
            return -1
        else:
            return 0
    else:
        return None
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # result = 0
    # action_r = actions(board)[0]
    # def max_value(board):
    #     v = -math.inf
    #     if(terminal(board) == True):
    #         return utility(board)
    #     for action in actions(board):
    #         v = max(v, min_value(result(board, action)+v))
    #         result = v
    #         if(result<v):
    #             action_r = action
    #     return v
    # def min_value(board):
    #     v = math.inf
    #     if(terminal(board) == True):
    #         return utility(board)
    #     for action in actions(board):
    #         v = min(v,max_value(result(board,action)+v))
    #         result = v
    #         if(result>v):
    #             action_r = action
    #     return v
    # if player(board) == "X":
    #     max_value(board)
    # elif player(board) == "O":
    #     min_value(board)
    # else:
    #     return None
    # return action_r
    # raise NotImplementedError
    if terminal(board):
        return None

    current = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = -math.inf
        best_action = None
        for action in actions(board):
            min_v, _ = min_value(result(board, action))
            if min_v > v:
                v = min_v
                best_action = action
        return v, best_action

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = math.inf
        best_action = None
        for action in actions(board):
            max_v, _ = max_value(result(board, action))
            if max_v < v:
                v = max_v
                best_action = action
        return v, best_action

    if current == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)
    return action