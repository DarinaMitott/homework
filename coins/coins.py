#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.


def max_sum_of_2(a: int, b: int, c: int) -> int:
    coins = [a, b, c]
    coins.sort(reverse=True)
    return coins[0] + coins[1]


def prompt_and_check(name) -> int:
    value = int(input(name + " = "))
    if value <= 0:
        raise Exception(f'u are invalid, ur variable {name} <= 0')
    return value


if __name__ == "__main__":
    a = prompt_and_check('a')
    b = prompt_and_check('b')
    c = prompt_and_check('c')

    print(max_sum_of_2(a, b, c))
