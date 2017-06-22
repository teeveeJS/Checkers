import copy
import math
import time

import checkers


def _value_of(piece, color):
    if piece is None:
        return 0
    value = 1 if piece.is_king else 0.5
    if piece.color != color:
        value = -value
    return value


def _heuristic(board):
    return sum([_value_of(tile, board.player_to_move)
                for row in board.tiles
                for tile in row])


def _negamax(board, a, b, depth_limit):
    winner = board.winner()
    if winner == board.player_to_move:
        return board, math.inf
    elif winner is not None:
        return board, -math.inf
    if depth_limit == 0:
        return board, _heuristic(board)

    best_move, best_val = None, -math.inf

    for move in checkers.possible_moves(board):
        next_board = copy.deepcopy(board)
        next_board.move(move)
        next_board.switch_player_to_move()
        val = -_negamax(next_board, -b, -a, depth_limit - 1)[1]
        if val > best_val:
            best_move = move
            best_val = val
        a = max(a, val)
        if a >= b:
            break
    return best_move, best_val


def make_move(board):
    return _negamax(board, -math.inf, math.inf, 6)[0]
