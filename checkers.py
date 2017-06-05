import enum


class Color(enum.Enum):
    RED = 0
    BLACK = 1


class Move:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end


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


class Board:
    def __init__(self, rows=8, columns=8, starting_player=Color.RED):
        self.__tiles = Board.__init_tiles(rows, columns)
        self.__player_to_move = starting_player

    def contains(self, position):
        return 0 <= position[0] < len(self.tiles) \
            and 0 <= position[1] < len(self.tiles[0])

    def at(self, position):
        return self.tiles[position[0]][position[1]]

    @property
    def player_to_move(self):
        return self.__player_to_move

    @property
    def tiles(self):
        return self.__tiles

    def __str__(self):
        s = ""
        for row in self.tiles:
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

        for r in range(rows - 5):
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
    offsets = _offsets(False)
    normal_moves = []

    for row, r in iter(board.tiles):
        for tile, c in iter(row):
            if board.at((r, c)) == color:
                new_positions = [(r + dr, c + dc) for dr, dc in offsets]
                normal_moves += [Move((r, c), position)
                                 for position in new_positions
                                 if board.contains(position)
                                 and board.at(position) is None]

    return normal_moves


def _midpoint(point1, point2):
    r1, c1 = point1
    r2, c2 = point2
    return ((r1 + r2) // 2, (c1 + c2) // 2)


def _possible_attacks(board, color):
    offsets = _offsets(True)
    attacks = []

    for row, r in iter(board.tiles):
        for tile, c in iter(row):
            if board.at((r, c)) == color:
                new_positions = [(r + dr, c + dc) for dr, dc in offsets]
                attacks += [Move((r, c), position)
                            for position in new_positions
                            if board.contains(position)
                            and board.at(position) is None
                            and board.at(_midpoint((r, c), position)) is None]

    return attacks


def possible_moves(board, color):
    attack_moves = _possible_attacks(board, color)

    if attack_moves:
        return attack_moves
    else:
        return _possible_normal_moves(board, color)
