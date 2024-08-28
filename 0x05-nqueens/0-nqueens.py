#!/usr/bin/python3
""" N queens puzzle, challenge of placing N non attacking queens
on a NxN chessboard
This program solves the N queens problem """

import sys


def is_safe(board, row, col, N):
    """ Check if a queen can be placed at position (row, col) """
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False

    # Check the left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check the right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N):
    """ Solve the N queens problem """
    def backtrack(row):
        """ Backtrack function to solve the problem """
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * N
    solutions = []
    backtrack(0)
    return solutions


def print_solutions(solutions, N):
    """ Print the solutions """
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)


if __name__ == "__main__":
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

    solutions = solve_nqueens(N)
    print_solutions(solutions, N)
