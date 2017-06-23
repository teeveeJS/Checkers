from abc import ABC, abstractmethod

import ai
from checkers import Board, Color, Move, possible_moves


def validate_move(move, board):
    return move in possible_moves(board)


class Player(ABC):
    def __init__(self, color):
        self.__color = color

    @abstractmethod
    def make_move(self, board):
        pass

    @property
    def color(self):
        return self.__color


class User(Player):
    def __init__(self, color):
        super().__init__(color)

    def make_move(self, board):
        while True:
            try:
                move_input = [int(s) for s in input().split(" ")]
                move = Move((move_input[0], move_input[1]),
                            (move_input[2], move_input[3]))
            except ValueError as e:
                print("ERROR: Invalid move format.")
                print("Move input should take the form: r1 c1 r2 c2.")
                print("Enter a move in that form: ", end="")
            else:
                if validate_move(move, board):
                    return move
                else:
                    print("ERROR: Illegal move entered.")
                    print("Enter a legal move: ", end="")


class AI(Player):
    def __init__(self, color):
        super().__init__(color)

    def make_move(self, board):
        return ai.make_move(board)


class Game:
    def __init__(self, red_type, black_type, board=Board()):
        self.__board = board
        self.__red_player = red_type(Color.RED)
        self.__black_player = black_type(Color.BLACK)

    def turn(self):
        print(self.__board)

        player, color = self.current_player()
        print("{0} to move: ".format(color), end="")
        if type(player) is AI:
            print("AI Input")

        move = player.make_move(self.__board)
        print(move)
        self.__board.move(move)

    def run(self):
        winner = None
        while winner is None:
            self.turn()
            self.__board.switch_player_to_move()
            winner = self.__board.winner()

    def current_player(self):
        if self.__board.player_to_move == Color.BLACK:
            return self.__black_player, "BLACK"
        else:
            return self.__red_player, "RED"
