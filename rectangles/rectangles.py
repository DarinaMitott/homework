#!/usr/bin/env python

"""
Даны два прямоугольника, стороны которых параллельны осям координат. Известны координаты левого нижнего угла x, y, а также ширина и высота прямоугольника w, h.

                w
    ┌───────────────────────┐
    │                       │
    │                       │ h
    │                       │
    └───────────────────────┘
 (x, y)

- определить, принадлежат ли все точки второго прямоугольника первому (`all`).
- определить, пересекаются ли эти прямоугольники (`any`, `all`).
"""

from collections import namedtuple

Rect = namedtuple("Rect", "x y w h")


def rect_inside(a: Rect, b: Rect) -> bool:
    """
    Checks if whole rectangle `b` is within rectangle `a`.
    """
    return all([
        b.x >= a.x,
        b.y >= a.y,
        b.x + b.w <= a.x + a.w,
        b.y + b.h <= a.y + a.h,
    ])


def rects_intersect(a: Rect, b: Rect) -> bool:
    """
    Checks if 2 rectangles `a` and `b` have at least a single intersection point.
    """
    return not any([
        a.x > b.x + b.w,
        a.x + a.w < b.x,
        a.y + a.h < b.y,
        a.y > b.y + b.h
    ])

