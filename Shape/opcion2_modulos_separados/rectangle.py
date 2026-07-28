"""Modulo independiente para la clase Rectangle."""

from .point import Point
from .line import Line
from .shape import Shape


class Rectangle(Shape):
    """Rectangulo definido de 4 formas distintas."""

    def __init__(self, **kwargs):
        if "width" in kwargs and "height" in kwargs and "center" in kwargs:
            self._width = kwargs["width"]
            self._height = kwargs["height"]
            self._center = kwargs["center"]

        elif "point1" in kwargs and "point2" in kwargs:
            self.point1 = kwargs["point1"]
            self.point2 = kwargs["point2"]
            self._width = abs(self.point2._x - self.point1._x)
            self._height = abs(self.point2._y - self.point1._y)
            center_x = (self.point1._x + self.point2._x) / 2
            center_y = (self.point1._y + self.point2._y) / 2
            self._center = Point(center_x, center_y)

        elif "width" in kwargs and "height" in kwargs and "bottom_left" in kwargs:
            self._width = kwargs["width"]
            self._height = kwargs["height"]
            self.bottom_left = kwargs["bottom_left"]
            center_x = self.bottom_left._x + self._width / 2
            center_y = self.bottom_left._y + self._height / 2
            self._center = Point(center_x, center_y)

        elif (
            "line1" in kwargs
            and "line2" in kwargs
            and "line3" in kwargs
            and "line4" in kwargs
        ):
            self.line1 = kwargs["line1"]
            self.line2 = kwargs["line2"]
            self.line3 = kwargs["line3"]
            self.line4 = kwargs["line4"]

            if self.line1.compute_length() == self.line2.compute_length():
                if self.line4.compute_length() == self.line3.compute_length():
                    self._width = self.line1.compute_length()
                    self._height = self.line3.compute_length()
                    center_x = (self.line1._start._x + self.line2._end._x) / 2
                    center_y = (self.line1._end._y + self.line2._start._y) / 2
                    self._center = Point(center_x, center_y)
                else:
                    raise ValueError("Parametros invalidos")

            elif self.line1.compute_length() == self.line3.compute_length():
                if self.line2.compute_length() == self.line4.compute_length():
                    self._width = self.line1.compute_length()
                    self._height = self.line4.compute_length()
                    center_x = (self.line1._end._x + self.line3._start._x) / 2
                    center_y = (self.line1._start._y + self.line3._end._y) / 2
                    self._center = Point(center_x, center_y)
                elif self.line1.compute_length() == self.line4.compute_length():
                    if self.line2.compute_length() == self.line3.compute_length():
                        self._width = self.line1.compute_length()
                        self._height = self.line3.compute_length()
                        center_x = (self.line1._start._x + self.line4._start._x) / 2
                        center_y = (self.line2._end._y + self.line4._end._y) / 2
                        self._center = Point(center_x, center_y)
                    else:
                        raise ValueError("Parametros invalidos")
            else:
                raise ValueError("Parametros invalidos")
        else:
            raise ValueError("Parametros invalidos")

        half_width = self._width / 2
        half_height = self._height / 2

        p1 = Point(self._center._x - half_width, self._center._y - half_height)
        p2 = Point(self._center._x + half_width, self._center._y - half_height)
        p3 = Point(self._center._x + half_width, self._center._y + half_height)
        p4 = Point(self._center._x - half_width, self._center._y + half_height)

        vertices = [p1, p2, p3, p4]
        edges = [Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)]
        inner_angles = [90, 90, 90, 90]
        is_regular = self._width == self._height

        super().__init__(is_regular, vertices, edges, inner_angles)

    def get_width(self):
        return self._width

    def set_width(self, new_width):
        self._width = new_width

    def get_height(self):
        return self._height

    def set_height(self, new_height):
        self._height = new_height

    def get_center(self):
        return self._center

    def set_center(self, new_center):
        self._center = new_center

    def compute_area(self) -> float:
        return self._width * self._height

    def __str__(self):
        return (
            f"Rectangle(width = {self._width}, height = {self._height}, "
            f"center = ({self._center._x}, {self._center._y}))"
        )
