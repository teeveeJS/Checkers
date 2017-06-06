from checkers import Board, Move, possible_moves


class Game:
    def __init__(self, board=Board()):
        self.__board = board
