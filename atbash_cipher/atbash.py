#!/usr/bin/env python

"""
Напишите программу, которая кодирует и декодирует текст шифром Атбаш.
В этом шифре каждая i-ая буква алфавита заменяется i-ой буквой с его конца, например, для латинского алфавита: a - z, b - y и т.д.

- заглавные буквы переводятся в строчные
- пробельные символы и знаки препинания опускаются
- шифр идёт блоками по 5 символов, между ними пробел

Пример:

`Bambarbia, Kirgudu` -> `yznyz iyrzp ritfw f`
"""
import string

BLOCK_SIZE = 5

ABC = string.ascii_lowercase
ATBASH_ABC = ABC[::-1]
IGNORE = set(string.punctuation + string.whitespace)


def atbash_encode(text: str) -> str:
    encoded = list()
    for character in text:
        character = character.lower()
        index = ABC.find(character)
        if index < 0:
            if character not in IGNORE:
                encoded.append(character)
        else:
            encoded.append(ATBASH_ABC[index])

    spaces = 0
    for p in range(5, len(encoded), 5):
        encoded.insert(p + spaces, ' ')
        spaces += 1

    return ''.join(encoded)


def atbash_decode(cipher: str) -> str:
    cipher = cipher.replace(' ', '')
    decoded = list()

    for character in cipher:
        index = ATBASH_ABC.find(character)
        if index < 0:
            decoded.append(character)
        else:
            decoded.append(ABC[index])

    return ''.join(decoded)
