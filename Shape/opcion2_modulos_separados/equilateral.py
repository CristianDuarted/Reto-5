"""Modulo independiente para la clase Equilateral."""

from .triangle import Triangle


class Equilateral(Triangle):
    """Triangulo con sus 3 lados iguales."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()
        if not (round(a, 5) == round(b, 5) == round(c, 5)):
            raise ValueError("No es un triangulo equilatero")
