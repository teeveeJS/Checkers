import enum


class Color(enum.Enum):
    RED = 0
    BLACK = 1


class Board:
    def __init__(self, rows=8, columns=8, starting_player=Color.RED):
        self.__tiles = Board.__init_tiles(rows, columns)
        self.__player_to_move = starting_player

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
                s += "R" if tile == Color.RED else \
                     "B" if tile == Color.BLACK else \
                     "-"
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
                if (r & 1) == (c & 1):
                    tiles[r][c] = Color.BLACK
                    tiles[rows - r - 1][columns - c - 1] = Color.RED
        return tiles
