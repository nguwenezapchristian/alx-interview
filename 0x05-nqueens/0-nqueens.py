#!/usr/bin/python3
"""
N Queens puzzle solver
"""

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""
    """ Check this row on left side """
    for i in range(col):
        if board[row][i] == 1:
            return False

    """ Check upper diagonal on left side """
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    """ Check lower diagonal on left side """
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """Utilize backtracking to solve the N Queens problem"""
    """ If all queens are placed """
    if col >= n:
        """ Add the solution to the list """
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0  # Backtrack


def solve_nqueens(n):
    """Main function to solve the N Queens problem"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions
