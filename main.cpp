#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

char board[8][8];
bool move_white = true;

class Move {
  int initRank, initFile, finRank, finFile;
  public:
    void set_values(int, int, int, int);
};

void initBoard() {
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      board[i][j] = 'o';
    }
  }
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 8; j++) {
      if (i % 2 == 0 && j % 2 == 0 || i % 2 != 0 && j % 2 != 0) {
          board[i][j] = 'x';
          board[7-i][7-j] = 'y';
        }
    }
  }
  cout<<"The board has been initialized\nWhite to move.\n";
}

void printBoard() {
  for (int i = 0; i < 8; i++) {
    char c = i;
    std::cout<<c + board[i]<<std::endl;
  }
}

int main() {
  initBoard();
  printBoard();
  /*
  while (true) {
    string move;
    cout<<"Enter your move";
    getline (cin, move);

  }*/
}
