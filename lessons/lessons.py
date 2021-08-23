#!/usr/bin/env python

"""
В школе, в которой учится В. Пупкин, занятия начинаются в 8 утра.
Урок длится 45 минут.
После каждого нечётного урока (1-го, 3-го, 5-го ...) перемена 5 минут,
а после каждого чётного (2-го, 4-го, 6-го ...) - 15.

Помогите непоседе Васе посчитать, когда заканчивается n-ый урок.
"""


def end_of_lesson(n: int) -> (int, int):
    if n <= 0:
        raise Exception('u entered incorrect number of lesson')
    if n == 1:
        return 8, 45
    spent = n * 45 + (n // 2) * 5 + ((n - 1) // 2) * 15
    h = 8 + spent // 60
    m = spent % 60
    return h, m


if __name__ == "__main__":
    n = int(input("Номер урока: "))

    hours, minutes = end_of_lesson(n)

    print(f"{n}-ый урок заканчивается в {hours}:{minutes:02}")
