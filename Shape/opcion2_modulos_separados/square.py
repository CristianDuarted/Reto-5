"""Modulo independiente para la clase Square."""

from .rectangle import Rectangle


class Square(Rectangle):
    """Caso particular de Rectangle donde width == height."""

    def __init__(self, side, center):
        super().__init__(width=side, height=side, center=center)
