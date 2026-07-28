"""Modulo independiente para la clase Line."""

import math

from .point import Point


class Line:
    """Representa un segmento de recta definido por dos puntos."""

    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end

    def get_start(self) -> Point:
        return self._start

    def set_start(self, new_start: Point):
        self._start = new_start

    def get_end(self) -> Point:
        return self._end

    def set_end(self, new_end: Point):
        self._end = new_end

    def compute_length(self) -> float:
        length = math.sqrt(
            (self._start._x - self._end._x) ** 2
            + (self._start._y - self._end._y) ** 2
        )
        return length

    def compute_slope(self):
        if self._end._x != self._start._x:
            slope = (self._start._y - self._end._y) / (self._start._x - self._end._x)
            angle = math.degrees(math.atan(slope))
            return angle
        else:
            return 90

    def compute_horizontal_cross(self) -> bool:
        if (self._end._y <= 0 and self._start._y >= 0) or (
            self._end._y >= 0 and self._start._y <= 0
        ):
            return True
        else:
            return False

    def compute_vertical_cross(self) -> bool:
        if (self._end._x <= 0 and self._start._x >= 0) or (
            self._end._x >= 0 and self._start._x <= 0
        ):
            return True
        else:
            return False
