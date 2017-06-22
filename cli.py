from checkers import Board, Color, Move, possible_moves


class Game:
    def __init__(self, board=Board()):
        self.__board = board

    def turn(self):
        while True:
            print(self.__board)
            print("{0} to move: "
                  .format("BLACK"
                          if self.__board.player_to_move == Color.BLACK
                          else "RED"),
                  end="")
            try:
                moveInput = [int(s) for s in input().split(" ")]
                move = Move((moveInput[0], moveInput[1]),
                            (moveInput[2], moveInput[3]))
            except Exception as e:
                print("ERROR:", e)
            else:
                if self.validate_move(move):
                    self.__board.move(move)
                    break

    def validate_move(self, move):
        return move in possible_moves(self.__board,
                                      self.__board.player_to_move)

    def run(self):
        winner = None
        while winner is None:
            self.turn()
            self.__board.switch_player_to_move()
            winner = self.__board.winner()
