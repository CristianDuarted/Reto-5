"""Modulo independiente para la clase Point."""


class Point:
    """Representa un punto (x, y) en el plano cartesiano."""

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def get_x(self) -> float:
        return self._x

    def set_x(self, new_x: float):
        self._x = new_x

    def get_y(self) -> float:
        return self._y

    def set_y(self, new_y: float):
        self._y = new_y

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"Point({self._x}, {self._y})"
