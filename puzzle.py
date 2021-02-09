"""
Module for validating puzzle game board.

Github:
https://github.com/ch1pkav/puzzle
"""

def read_file(path) -> list:
    """
    Reads board file and returns it as a list.
    """

    board_file = open(path, "r")
    board = [row[:-1] for row in board_file.readlines()]

    return board


def check_for_duplicates(row: list) -> bool:
    """
    Receives a list of numbers and checks them for duplicates
    """

    if len(set(row)) == len(row):
        return True
    return False


def check_rows(board: list) -> bool:
    """
    Checks rows of the board for duplicate or outlying numbers
    """

    for row in board:
        num_list = []
        for char in row:
            if ord(char) in range(49, 58):
                num_list.append(char)
        if not check_for_duplicates(num_list):
            return False
    return True


def flip_board(board: list) -> list:
    """
    Flips board for easier vertical checking.
    """

    dimensions = 9
    flipped_board = []

    for i in range(dimensions):

        row = ""
        for j in range(dimensions):
            row += board[j][i]

        flipped_board.append(row)

    return flipped_board


def check_fields(board: list, flipped_board: list):
    """
    Parses fields from the board and the flipped board and checks them for duplicates
    """

    field_board = [] #The field board is just a list of fields converted into strings

    for i in range(5): #Flipped board is used here for easier field parsing
        field = board[i+4][4-i:9-i] + flipped_board[4-i][i:i+4]
        field_board.append(field)

    return check_rows(field_board)


def validate_board(board):
    """
    Checks rows and columns by flipping the board, checks fields using the flipped board.
    """

    flipped_board = flip_board(board)

    if not (check_rows(board) and check_rows(flipped_board) and check_fields(board, flipped_board)):
        return False

    return True

