"""Modulo independiente para la clase TriRectangle."""

from .triangle import Triangle


class TriRectangle(Triangle):
    """Triangulo rectangulo: cumple el teorema de Pitagoras."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()
        lados = sorted([a, b, c])
        if not (lados[0] ** 2 + lados[1] ** 2 == lados[2] ** 2):
            raise ValueError("No es un triangulo rectangulo")
