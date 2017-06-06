def value_of(piece, color):
    if piece is None:
        return 0

    value = 1 if piece.is_king else 0.5
    if piece.color != color:
        value = -value
    return value


def heuristic(self, board, color):
    return sum([value_of(tile, color) for tile in board.tiles])


def negamax(self, board, a, b, depth_limit):
    raise NotImplementedError
