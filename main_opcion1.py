"""
main_opcion1.py
===============

Version alterna de main.py que usa la Opcion 1 del paquete Shape
(todas las clases en un unico modulo: shapes.py).
"""

import math

from Shape.opcion1_modulo_unico import (
    Point,
    Rectangle,
    Triangle,
    TriRectangle,
    Isosceles,
    Scalene,
    Equilateral,
)


def main():
    print("=== RECTANGLE ===")
    r = Rectangle(width=10, height=5, center=Point(0, 0))
    print(f"Area rectangulo: {r.compute_area()}")
    print(f"Perimetro rectangulo: {r.compute_perimeter()}")
    print(f"Vertices rectangulo: {r.get_vertices()}")

    print("\n=== SQUARE ===")
    s = Rectangle(width=4, height=4, center=Point(0, 0))
    print(f"Area cuadrado: {s.compute_area()}")
    print(f"Perimetro cuadrado: {s.compute_perimeter()}")
    print(f"Es regular?: {s.get_is_regular()}")

    print("\n=== TRIANGLE 3-4-5 ===")
    t = Triangle(vertice1=Point(0, 0), vertice2=Point(4, 0), vertice3=Point(0, 3))
    print(f"Area triangulo: {t.compute_area()}")
    print(f"Perimetro triangulo: {t.compute_perimeter()}")
    print(f"Vertices triangulo: {t.get_vertices()}")

    print("\n=== TRI-RECTANGLE ===")
    tr = TriRectangle(
        vertice1=Point(0, 0), vertice2=Point(4, 0), vertice3=Point(0, 3)
    )
    print(f"Area triangulo rectangulo: {tr.compute_area()}")
    print(f"Perimetro triangulo rectangulo: {tr.compute_perimeter()}")

    print("\n=== ISOSCELES ===")
    iso = Isosceles(
        vertice1=Point(0, 0), vertice2=Point(4, 0), vertice3=Point(2, 3)
    )
    print(f"Area isosceles: {iso.compute_area()}")
    print(f"Perimetro isosceles: {iso.compute_perimeter()}")

    print("\n=== SCALENE ===")
    sca = Scalene(
        vertice1=Point(0, 0), vertice2=Point(4, 0), vertice3=Point(1, 3)
    )
    print(f"Area escaleno: {sca.compute_area()}")
    print(f"Perimetro escaleno: {sca.compute_perimeter()}")

    print("\n=== EQUILATERAL ===")
    eq = Equilateral(
        vertice1=Point(0, 0),
        vertice2=Point(2, 0),
        vertice3=Point(1, math.sqrt(3)),
    )
    print(f"Area equilatero: {eq.compute_area()}")
    print(f"Perimetro equilatero: {eq.compute_perimeter()}")
    print(f"Es regular?: {eq.get_is_regular()}")


if __name__ == "__main__":
    main()
