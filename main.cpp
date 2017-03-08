#include <cstdlib>
#include <iostream>
//#include <string>
#include <math.h>

using namespace std;

bool move_white = true;

class Bitboard {
  char board [32];
  public:
    void init(void);
    char * printBoard(void);
    //bool isLegal();
    //two options for making the move: new Bitboard or update the current
    //e.g. void/Bitboard updateBoard()
};

void Bitboard::init() {
  for (int i = 0; i < 12; i++) {
    board[i] = 'x'; //white pieces
    board[31-i] = 'y'; //black pieces
    if (i < 8) {
      board[12 + i] = 'o'; //empty squares
    }
  }
  std::cout << "The board has been initialized\n" << std::endl;
  //could return board for function chaining idk
}

char * Bitboard::printBoard() {
  static char tempBoard [73]; //9x8 (+1 for null character at the end)
  tempBoard[72] = '\0';
  for (int i = 0; i < 72; i++) {
    if ( ((i + 1) % 9) == 0) {
      tempBoard[i] = '\n';
    } else if ( (i % 2) == 0) {
      tempBoard[i] = 'o';
    } else {
      int conversion = (i - (1 + floor(i) * 2)) / 2;
      //there's definitely something more elegant
      tempBoard[i] = board[conversion];
    }
  }
  return tempBoard;
}

class Move {
  int initRank, initFile, finRank, finFile;
  public:
    void setValues(int, int, int, int); //maybe a string instead
};

void Move::setValues(int iR, int iF, int fiR, int fiF) {
  initRank = iR;
  initFile = iF;
  finRank = fiR;
  finFile = fiF;
}

int main() {
  Bitboard test;
  test.init();

  char *b;
  b = test.printBoard();
  std::cout << *b << std::endl;

  std::cout << "test over" << std::endl;
  /*
  while (true) {
    string move;
    cout<<"Enter your move";
    getline (cin, move);

  }*/
  return 0;
}
