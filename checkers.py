import enum


class Color(enum.Enum):
    RED = 0
    BLACK = 1

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


class Move:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def is_attack(self):
        def diff2(val1, val2):
            return abs(val1 - val2) == 2

        return diff2(self.start[0], self.end[0]) \
            and diff2(self.start[1], self.end[1])

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "{0} -> {1}".format(self.start, self.end)


class Piece:
    def __init__(self, color):
        self.__color = color
        self.__is_king = False

    def promote(self):
        self.__is_king = True

    @property
    def color(self):
        return self.__color

    @property
    def is_king(self):
        return self.__is_king


def _midpoint(point1, point2):
    r1, c1 = point1
    r2, c2 = point2
    return ((r1 + r2) // 2, (c1 + c2) // 2)


class Board:
    def __init__(self, rows=8, columns=8, starting_player=Color.RED):
        self.__tiles = Board.__init_tiles(rows, columns)
        self.__player_to_move = starting_player

    def move(self, move):
        if move.is_attack():
            mid = _midpoint(move.start, move.end)
            self.__tiles[mid[0]][mid[1]] = None
        self.__tiles[move.end[0]][move.end[1]] = self.at(move.start)
        self.__tiles[move.start[0]][move.start[1]] = None

    def switch_player_to_move(self):
        if self.player_to_move == Color.RED:
            self.__player_to_move = Color.BLACK
        else:
            self.__player_to_move = Color.RED

    def contains(self, position):
        return 0 <= position[0] < len(self.tiles) \
            and 0 <= position[1] < len(self.tiles[0])

    def at(self, position):
        return self.tiles[position[0]][position[1]]

    def winner(self):
        n_black_pieces = 0
        n_red_pieces = 0

        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    if tile.color == Color.RED:
                        n_red_pieces += 1
                    elif tile.color == Color.BLACK:
                        n_black_pieces += 1

        if n_black_pieces == 0:
            return Color.RED
        elif n_red_pieces == 0:
            return Color.BLACK
        else:
            return None

    @property
    def rows(self):
        return len(self.tiles)

    @property
    def columns(self):
        return len(self.tiles[0])

    @property
    def player_to_move(self):
        return self.__player_to_move

    @property
    def tiles(self):
        return self.__tiles

    def __str__(self):
        s = "  " + " ".join(str(c) for c in range(self.columns)) + "\n\n"
        for r, row in enumerate(self.tiles):
            s += str(r) + " "
            for tile in row:
                if tile is None:
                    s += "-"
                else:
                    c = "b" if tile.color == Color.BLACK else "r"
                    s += c.upper() if tile.is_king else c
                s += " "
            s += "\n\n"
        return s

    @staticmethod
    def __init_tiles(rows, columns):
        if (rows & 1) == 1 or (columns & 1) == 1:
            raise ValueError("rows and columns should both be even")
        if rows <= 0 or columns <= 0:
            raise ValueError("rows and columns should both be positive")

        tiles = [[None for _ in range(columns)] for _ in range(rows)]

        for r in range(rows // 2 - 1):
            for c in range(columns):
                if (r & 1) != (c & 1):
                    tiles[r][c] = Piece(Color.BLACK)
                    tiles[rows - r - 1][columns - c - 1] = Piece(Color.RED)
        return tiles


def _offsets(is_attack, color, is_king):
    offset = 2 if is_attack else 1
    dcs = [-offset, offset]
    if is_king:
        drs = dcs
    elif color == Color.RED:
        drs = [-offset]
    else:
        drs = [offset]
    return [(dr, dc) for dr in drs for dc in dcs]


def _possible_normal_moves(board, color):
    normal_moves = []

    for r, row in enumerate(board.tiles):
        for c, tile in enumerate(row):
            if tile is not None and tile.color == color:
                offsets = _offsets(False, color, tile.is_king)
                new_positions = [(r + dr, c + dc) for dr, dc in offsets]
                normal_moves += [Move((r, c), position)
                                 for position in new_positions
                                 if board.contains(position)
                                 and board.at(position) is None]

    return normal_moves


def _possible_attacks(board, color):
    attacks = []

    for r, row in enumerate(board.tiles):
        for c, tile in enumerate(row):
            if tile is not None and tile.color == color:
                offsets = _offsets(True, color, tile.is_king)
                new_positions = [(r + dr, c + dc) for dr, dc in offsets]
                for position in new_positions:
                    if board.contains(position) and board.at(position) is None:
                        mid_tile = board.at(_midpoint((r, c), position))
                        if mid_tile is not None and mid_tile.color != color:
                            attacks.append(Move((r, c), position))

    return attacks


def possible_moves(board):
    color = board.player_to_move
    attack_moves = _possible_attacks(board, color)

    if attack_moves:
        return attack_moves
    else:
        return _possible_normal_moves(board, color)
