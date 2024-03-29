from typing import List
from line import Line


class Square:
    """
    Класс для работы заданным квадратом рабочей области

    Аттрибуты:
        coordinates: Координаты квадрата в рабочей области
        lines: Линии, которые проходят через заданный квадрат
    """
    coordinates: List[int]
    lines: List[Line]

    def __init__(self, x: int, y: int):
        """
        :param x: Координата x квадрата в рабочей области
        :param y Координата y квадрата в рабочей области
        """
        self.coordinates = [x, y]
        self.lines = []
