#!/usr/bin/env python
from math import pi


# Бабушка Зина любит печь блины своему любимому внуку Васе.
# А внук Вася любит математику и знает, что периметр и площадь блина можно найти по диаметру сковородки.
# Напишите программу, которая поможет Васе проверить его вычисления.


def perimeter(diameter):
    return pi * diameter


def square(diameter):
    return pi * (diameter / 2) ** 2


if __name__ == "__main__":
    d = int(input("Диаметр сковородки = "))

    print(perimeter(d))
    print(square(d))
