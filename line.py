import math
from point import Point


class Line:
    """
    Класс для работы с линией

    Аттрибуты:
        first_point: Первая точка, задающая линию
        second_point: Вторая точка, задающая линию
        angle_tangent: Тангенс угла между линией и осью x
    """
    first_point: Point
    second_point: Point
    angle: float

    def __init__(self, first_point: Point, second_point: Point):
        """
        Конструктор класса

        :param first_point: Первая точка, задающая линию
        :param second_point: Вторая точка, задающая линию
        """
        self.first_point = first_point
        self.second_point = second_point

        # Определим угол наклона линии
        x1: float = first_point.x
        y1: float = first_point.y
        x2: float = second_point.x
        y2: float = second_point.y
        cathetus_x: float = abs(x2 - x1)
        cathetus_y: float = abs(y2 - y1)
        self.angle = math.atan(cathetus_y / cathetus_x)

    def print_line_points(self):
        """
        Метод для вывода координат точек линии
        """
        print(f'Первая точка: ({self.first_point.x}; {self.first_point.y})')
        print(f'Вторая точка: ({self.second_point.x}; {self.second_point.y})')

