"""
Opcion 2: un modulo independiente por clase.

Expone todas las clases a nivel de paquete para poder importarlas como:

    from Shape.opcion2_modulos_separados import Rectangle, Triangle, ...
"""

from .point import Point
from .line import Line
from .shape import Shape
from .rectangle import Rectangle
from .square import Square
from .triangle import Triangle
from .equilateral import Equilateral
from .isosceles import Isosceles
from .scalene import Scalene
from .tri_rectangle import TriRectangle

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
