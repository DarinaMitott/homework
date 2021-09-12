#!/usr/bin/env python

"""
Напишите функцию, которая возвращает для чисел:

- кратных 3 -
- кратных 5 - Buzz
- одновременно кратных и 3 и 5 - FizzBuzz
- строковое представление этих чисел (т.е. "1" для 1)

https://en.wikipedia.org/wiki/Fizz_buzz
"""


def fizzbuzz(n: int) -> str:
    if n == 0:
        raise ValueError("Number must be a positive integer")
    multiple3 = n % 3 == 0
    multiple5 = n % 5 == 0
    if multiple5 and multiple3:
        return 'FizzBuzz'

    if multiple3:
        return 'Fizz'

    if multiple5:
        return 'Buzz'

    return str(n)

