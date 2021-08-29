#!/usr/bin/env python

"""
Напишите функцию, которая проверяет "силу" пароля.

Надёжный пароль:
    - не менее 10 символов
    - содержит буквы разного регистра
    - минимум одну цифру
    - минимум один знак пунктуации
"""
import string


def is_strong_password(pwd: str) -> bool:
    if len(pwd) < 10:
        return False

    uppercase = False
    lowercase = False
    number = False
    punctuation = False

    for e in pwd:
        if e.isupper():
            uppercase = True
        if e.islower():
            lowercase = True
        if e.isdigit():
            number = True
        if e in string.punctuation:
            punctuation = True

    return uppercase and lowercase and number and punctuation

