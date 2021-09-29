#!/usr/bin/env python

"""
Напишите функции для вывода ходов шахматных фигур на пустой доске.

Например, для коня на поле a1 доступных полей будет 2: b3 и с2,
а для ладьи на поле a1 будут доступны вся вертикаль a и 1-ая горизонталь.
"""

abc = 'abcdefgh'


def square_to_point(square):
    col = abc.index(square[0])
    row = int(square[1]) - 1
    return col, row


def rook_moves(square: str) -> list:
    col, row = square_to_point(square)
    moves = list()
    for i_row in range(8):
        for i_col in range(8):
            if (i_row == row and i_col != col) or (i_row != row and i_col == col):
                moves.append(abc[i_col] + str(i_row + 1))
    return moves


def bishop_moves(square: str) -> list:
    col, row = square_to_point(square)
    moves = list()
    steps = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i_dig in range(1, 8):
        for col_inc, row_inc in steps:
            n_col = col + col_inc * i_dig
            if n_col < 0 or n_col >= 8:
                continue
            n_row = row + row_inc * i_dig
            if n_row < 0 or n_row >= 8:
                continue

            moves.append(abc[n_col] + str(n_row + 1))

    return moves


def queen_moves(square: str) -> list:
    col, row = square_to_point(square)
    moves = list()
    steps = [
        # diagonal increments
        (1, 1), (1, -1), (-1, 1), (-1, -1),
        # vert/horiz increments
        (1, 0), (-1, 0), (0, 1), (0, -1),
    ]

    for i_dig in range(1, 8):
        for col_inc, row_inc in steps:
            n_col = col + col_inc * i_dig
            if n_col < 0 or n_col >= 8:
                continue
            n_row = row + row_inc * i_dig
            if n_row < 0 or n_row >= 8:
                continue

            moves.append(abc[n_col] + str(n_row + 1))

    return moves


def knight_moves(square: str) -> list:
    col, row = square_to_point(square)
    moves = list()
    steps = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2),
    ]

    for col_inc, row_inc in steps:
        n_col = col + col_inc
        if n_col < 0 or n_col >= 8:
            continue
        n_row = row + row_inc
        if n_row < 0 or n_row >= 8:
            continue

        moves.append(abc[n_col] + str(n_row + 1))

    return moves


def king_moves(square: str) -> list:
    col, row = square_to_point(square)
    moves = list()
    for i_row in range(max(row - 1, 0), min(row + 2, 8)):
        for i_col in range(max(col - 1, 0), min(col + 2, 8)):
            if i_row != row or i_col != col:
                moves.append(abc[i_col] + str(i_row + 1))
    return moves
