#include "Board.hpp"

Board::Board() : playerToMove_(WHITE)
{
    initBoard();
}

const std::array<std::array<Color, 8>, 8> &Board::board() const
{
    return board_;
}

Color Board::playerToMove() const
{
    return playerToMove_;
}

std::ostream &operator<<(std::ostream &out, const Board &board)
{
    for (auto row : board.board())
    {
        for (auto color : row)
        {
            out << ColorStrings[color];
        }
        out << std::endl;
    }
    return out;
}

void Board::initBoard()
{
    for (unsigned int i = 0; i < board().size(); i++)
    {
        for (unsigned int j = 0; j < board().size(); j++)
        {
            board_[i][j] = NONE;
        }
    }
    for (unsigned int i = 0; i < 3; i++)
    {
        for (unsigned int j = 0; j < board().size(); j++)
        {
            if ((i & 1) == (j & 1))
            {
                board_[i][j] = WHITE;
                board_[7 - i][7 - j] = BLACK;
            }
        }
    }
}
