#!/usr/bin/env python

"""
Реализовать функцию `get_ranges` которая “сворачивает” список неповторяющихся целых чисел, отсортированных по возрастанию:

- [0, 1, 2, 3, 4, 7, 8, 10] -> "0-4, 7-8, 10"
- [4, 7, 10] -> "4, 7, 10"
- [2, 3, 8, 9]) -> "2-3, 8-9"
"""


def get_ranges(l: list) -> str:
    l = sorted(set(l))
    ranges = []
    current = None
    for i in range(len(l)):
        if not current:
            current = [l[i], l[i]]
            continue
        if l[i] - 1 == current[1]:
            current[1] = l[i]
        else:
            ranges.append(f'{current[0]}-{current[1]}' if current[0] != current[1] else str(current[0]))
            current = [l[i], l[i]]
    if current:
        ranges.append(f'{current[0]}-{current[1]}' if current[0] != current[1] else str(current[0]))
    return ', '.join(ranges)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 9]))
