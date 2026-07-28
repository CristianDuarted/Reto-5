"""Modulo independiente para la clase base Shape."""


class Shape:
    """Clase base abstracta de la que heredan todas las figuras."""

    def __init__(
        self,
        is_regular: bool,
        vertices: list,
        edges: list,
        inner_angles: list,
    ):
        self._is_regular = is_regular
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def get_is_regular(self):
        return self._is_regular

    def set_is_regular(self, new_is_regular):
        self._is_regular = new_is_regular

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, new_vertices):
        self._vertices = new_vertices

    def get_edges(self):
        return self._edges

    def set_edges(self, new_edges):
        self._edges = new_edges

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, new_inner_angles):
        self._inner_angles = new_inner_angles

    def compute_area(self):
        pass

    def compute_perimeter(self) -> float:
        perimeter = 0
        for edge in self._edges:
            perimeter += edge.compute_length()
        return perimeter

    def compute_inner_angles(self):
        pass
