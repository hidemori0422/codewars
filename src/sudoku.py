#! /usr/bin/env python3

def done_or_not(board):
    """Checks the given matrix and returns whether the sudoku board is complete.

    Args:
        board (list): List of list. Represents the sudoku board.

    Returns:
        'Finished!' if the board is complete, 'Try again!' otherwise.
    """
    board_size = 9
    complete_array = [n+1 for n in range(board_size)]
    for i in range(board_size):
        # check rows
        if sorted(board[i]) != complete_array:
            return 'Try again!'
        # check array
        if sorted([board[j][i] for j in range(board_size)]) != complete_array:
            return 'Try again!'
    # check inside square
    for i in range(int(board_size / 3)):
        for j in range(int(board_size / 3)):
            start = 3*j
            end = 3*(j+1)
            square = board[3*i][start:end] + board[3*i+1][start:end] + board[3*i+2][start:end]
            if sorted(square) != complete_array:
                return 'Try again!'
    return 'Finished!'


if __name__ == '__main__':
    print('Module codewars/src/sudoku.py')
