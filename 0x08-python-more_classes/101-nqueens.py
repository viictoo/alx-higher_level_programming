#!/usr/bin/python3
"""
The N queens puzzle is the challenge of
placing N non-attacking queens on an N×N
chessboard. This is a program that solves
the N queens problem.

Usage: ./101-nqueens.py N
    N must be a number(at least 4)

backtracking: abandons a candidate as soon as it determines
that the candidate cannot possibly be completed to a valid solution

queen movement: It can move any number of squares
vertically, horizontally or diagonally

"""
import sys


def is_secure(chess_board, row, clm):
    """checks if it is safe to place the queen in position depending
    on whether there is another queen in the same colum or diagonals

    Args:
        chess_board (list of lists): repr chess board
        row (list): rows
        col (list): columns
    returns true if it is safe
    """
    """Check upper right diagonal"""
    i = row - 1
    j = clm + 1
    while i >= 0 and j < N:
        if chess_board[i][j] == 1:
            return False
        i -= 1
        j += 1
    """Check upper left diagonal"""
    i = row - 1
    j = clm - 1
    while i >= 0 and j >= 0:
        if chess_board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    """Check same column"""
    for i in range(row):
        if chess_board[i][clm] == 1:
            return False

    return True


def print_nqueens(board):
    """Prints the solution

    Args:
        board (list of lists): chess board
    """
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])

    print(solution)


def recursive_nqueens_solv(grid, row):
    """solves N-Queens using recursion
    """
    """Base: all queens are placed, print the solution"""
    if row == N:
        print_nqueens(grid)
        return

    """try placing a queen in each col of the current row"""
    for col in range(N):
        if is_secure(grid, row, col):
            grid[row][col] = 1
            recursive_nqueens_solv(grid, row + 1)
            """backtrack"""
            grid[row][col] = 0


if __name__ == '__main__':
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

    board = [[0] * N for _ in range(N)]

    recursive_nqueens_solv(board, 0)
