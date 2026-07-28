"""
Opcion 1: modulo unico.

Expone todas las clases del modulo ``shapes`` a nivel de paquete para
que puedan importarse como:

    from Shape.opcion1_modulo_unico import Rectangle, Triangle, ...
"""

from .shapes import (
    Point,
    Line,
    Shape,
    Rectangle,
    Square,
    Triangle,
    Equilateral,
    Isosceles,
    Scalene,
    TriRectangle,
)

__all__ = [
    "Point",
    "Line",
    "Shape",
    "Rectangle",
    "Square",
    "Triangle",
    "Equilateral",
    "Isosceles",
    "Scalene",
    "TriRectangle",
]
