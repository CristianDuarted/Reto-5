"""Modulo independiente para la clase Scalene."""

from .triangle import Triangle


class Scalene(Triangle):
    """Triangulo con sus 3 lados distintos."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()
        if a == b or b == c or a == c:
            raise ValueError("No es un triangulo escaleno")
