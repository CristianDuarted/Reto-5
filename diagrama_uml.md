# Diagrama UML — Paquete Shape

```mermaid
classDiagram
    class Point {
        -_x: float
        -_y: float
        +get_x() float
        +set_x(new_x)
        +get_y() float
        +set_y(new_y)
    }

    class Line {
        -_start: Point
        -_end: Point
        +get_start() Point
        +set_start(new_start)
        +get_end() Point
        +set_end(new_end)
        +compute_length() float
        +compute_slope() float
        +compute_horizontal_cross() bool
        +compute_vertical_cross() bool
    }

    class Shape {
        -_is_regular: bool
        -_vertices: list~Point~
        -_edges: list~Line~
        -_inner_angles: list~float~
        +get_is_regular() bool
        +get_vertices() list
        +get_edges() list
        +get_inner_angles() list
        +compute_area()
        +compute_perimeter() float
        +compute_inner_angles()
    }

    class Rectangle {
        -_width: float
        -_height: float
        -_center: Point
        +get_width() float
        +get_height() float
        +get_center() Point
        +compute_area() float
    }

    class Square

    class Triangle {
        -line1: Line
        -line2: Line
        -line3: Line
        +compute_area() float
    }

    class Equilateral
    class Isosceles
    class Scalene
    class TriRectangle

    Shape <|-- Rectangle
    Rectangle <|-- Square
    Shape <|-- Triangle
    Triangle <|-- Equilateral
    Triangle <|-- Isosceles
    Triangle <|-- Scalene
    Triangle <|-- TriRectangle

    Line --> Point : usa
    Shape --> Point : contiene
    Shape --> Line : contiene
