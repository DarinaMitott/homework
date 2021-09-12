#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""
import math


def rev(num):
    return int(num != 0) and ((num % 10) * (10 ** int(math.log(num, 10))) + rev(num // 10))


def is_palindrom(n: int) -> bool:
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    return n == rev(n)

