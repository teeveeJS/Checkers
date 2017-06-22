import ai
import checkers


def main():
    board = checkers.Board()
    print(board)
    board.move(ai.make_move(board))
    print(board)


if __name__ == "__main__":
    main()
