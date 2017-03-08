all: gcc

gcc:
	g++ *.cpp -o Checkers.exe -std=c++14 -Wall
    
clang:
	clang++ *.cpp -o Checkers.exe -std=c++14 -Wall
