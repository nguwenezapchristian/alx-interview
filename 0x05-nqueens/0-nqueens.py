#!/usr/bin/python3
import sys
"""
N Queens problem

This script solves the N Queens problem
and prints all possible solutions

Usage: nqueens N
N must be an integer greater than or equal to 4
N must be greater than 0
"""


def is_valid(board, row, col):
    """ Check if a queen can be placed on board at row, col """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """ Solve the N Queens problem and print all solutions """
    def backtrack(row):
        if row == N:
            solution = []
            for i in range(N):
                solution.append([i, board[i]])
            solutions.append(solution)
        else:
            for col in range(N):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(row + 1)

    board = [-1] * N
    solutions = []
    backtrack(0)
    for solution in solutions:
        print(solution)


def main():
    """ Main function to parse command line arguments and solve N Queens """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    """ Main function to parse command line arguments and solve N Queens """
    main()
