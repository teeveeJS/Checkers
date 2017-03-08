struct Move
{
public:
    const unsigned int START_ROW; //maybe use std::pair instead ?
    const unsigned int START_COLUMN; //these are not meant to be negative
    const unsigned int END_ROW;
    const unsigned int END_COLUMN;
    Move(unsigned int startRow, unsigned int startColumn,
         unsigned int endRow, unsigned int endColumn)
        : START_ROW(startRow), START_COLUMN(startColumn),
          END_ROW(endRow), END_COLUMN(endColumn) {}

};
