#!/usr/bin/env python

"""
Напишите функцию, которая принимает на вход строку `s` и некоторый сепаратор `sep`.
Функция должна удалить из строки всё, что находится между первым и последним сепаратором, а также их самих.
Если таких сеператоров в строке меньше двух, вернуть исходную строку.
"""


def remove_fragment(s: str, sep: str) -> str:
    start = s.find(sep)
    if start < 0:
        return s

    end = s.rfind(sep)
    if start == end:
        return s

    return s[:start] + s[end + len(sep):]

