#!/usr/bin/env python

"""
Напишите программу, которая использует шахматную нотацию Форсайта-Эдвардса (FEN - Forsyth–Edwards Notation)
для подсчёта баланса материала между белыми и чёрными.

- https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
- https://ru.wikipedia.org/wiki/Нотация_Форсайта_—_Эдвардса
- https://www.chessprogramming.org/Forsyth-Edwards_Notation

FEN задаёт полное расположение фигур на доске.
Относительная ценность фигур задана константами.
"""

PAWN_VAL = 1  # пешка
KNIGHT_VAL = BISHOP_VAL = 3  # конь и слон
ROOK_VAL = 5  # ладья
QUEEN_VAL = 9  # ферзь

CHESS = {'p': PAWN_VAL, 'n': KNIGHT_VAL, 'b': BISHOP_VAL, 'r': ROOK_VAL, 'q': QUEEN_VAL}


def calc_chess_balance(fen: str) -> int:
    result = 0
    for character in fen.split(' ')[0]:
        if character.lower() in 'rnbqp':
            if character.isupper():
                result += CHESS[character.lower()]
            else:
                result -= CHESS[character.lower()]
    return result
