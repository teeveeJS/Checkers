#ifndef BOARD_H

#define BOARD_H

#include <array>
#include <ostream>
#include <string>

enum Color { WHITE, BLACK, NONE };
const std::string ColorStrings[] { "x", "y", "o" };

class Board //should probably name it something smarter than board
{
public:
    Board();
    const std::array<std::array<Color, 8>, 8> &board() const;
    Color playerToMove() const;
    friend std::ostream &operator<<(std::ostream &out, const Board &board);
private:
    std::array<std::array<Color, 8>, 8> board_;
    Color playerToMove_;
    void initBoard();
};

#endif
