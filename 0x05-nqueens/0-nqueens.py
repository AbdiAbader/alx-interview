#!/usr/bin/python3
""" N queens puzzle USES backtracking to solve the problem """
import sys


def is_safe(board, row, col):
    """ Check if a queen can be placed on board[row][col]"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def backtracking(board, row, n, solutions):
    """ Solve the N queens puzzle USING RECURSION METHOD CALLED BACKTRACKING"""
    if row == n:
        solutions.append(board.copy())
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            print(board)
            backtracking(board, row + 1, n, solutions)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def main():
    """ Main function """
    solutions = []
    board = [-1] * n
    backtracking(board, 0, n, solutions)


if __name__ == "__main__":
    main()
