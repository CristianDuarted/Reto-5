"""Modulo independiente para la clase Triangle."""

import math

from .line import Line
from .shape import Shape


class Triangle(Shape):
    """Triangulo definido por 3 vertices."""

    def __init__(self, **kwargs):
        p1 = kwargs["vertice1"]
        p2 = kwargs["vertice2"]
        p3 = kwargs["vertice3"]

        vertices = [p1, p2, p3]

        self.line1 = Line(p1, p2)
        self.line2 = Line(p2, p3)
        self.line3 = Line(p3, p1)
        edges = [self.line1, self.line2, self.line3]

        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()

        if round(a, 5) == round(b, 5) == round(c, 5):
            is_regular = True
        else:
            is_regular = False

        inner_angles = []

        super().__init__(is_regular, vertices, edges, inner_angles)

    def compute_area(self) -> float:
        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()
        semiperimetro = (a + b + c) / 2
        area = math.sqrt(
            semiperimetro
            * (semiperimetro - a)
            * (semiperimetro - b)
            * (semiperimetro - c)
        )
        return area
