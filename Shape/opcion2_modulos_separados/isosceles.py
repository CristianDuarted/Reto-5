"""Modulo independiente para la clase Isosceles."""

from .triangle import Triangle


class Isosceles(Triangle):
    """Triangulo con al menos 2 lados iguales."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()
        if not (a == b or b == c or a == c):
            raise ValueError("No es un triangulo isosceles")
