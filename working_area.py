from typing import List, Tuple
import numpy as np
from line import Line
from square import Square
import geometry


class WorkingArea:
    """
    Класс, который хранит в себе информацию рабочей области: положение линий и др.

    Аттрибуты:
        lines: Линии, проходящие через рабочую область
        working_area_limits: Пределы рабочей области - минимальные и максимальные значения по x и по y
        squares: Двумерный список квадратов рабочей области
    """
    lines: List[Line]
    working_area_limits: List[int]
    squares: List[List[Square]]

    def __init__(self, lines: List[Line], working_area_limits: List[int]):
        """
        Конструктор класса

        :param lines: Список линий, проходящих через рабочую область
        :param working_area_limits: Пределы рабочей области - минимальные и максимальные значения по x и по y
        """
        self.lines = lines
        self.working_area_limits = working_area_limits

        working_area_shape: List[int] = self.get_working_area_shape()

        # Инициализация двумерного массива квадратов
        self.squares = []
        for i in range(working_area_shape[0]):
            self.squares.append([])
            for j in range(working_area_shape[1]):
                self.squares[i].append(Square(i, j))

        # Определим для каждого квадрата индексы линий, которые через него проходят
        self.calculate_lines_for_all_squares()

        # Уберём из квадратов линии, которые имеют слишком маленьний угол между друг другом.
        self.filtrate_parallel_lines()

    def get_working_area_shape(self):
        working_area_shape: List[int] = [
            abs(self.working_area_limits[1] - self.working_area_limits[0]),
            abs(self.working_area_limits[3] - self.working_area_limits[2])
        ]
        return working_area_shape

    def filtrate_parallel_lines(self):
        """
        Удалить из списков с индексами линий, проходящих через заданный квадрат, индексы тех линий, которые имеют
        малое отличие по углу наклона. То есть вот у нас есть квадрат. И мы имеем список индексов линий, которые
        через него проходят. И некоторые линии имеют малое различие по углу наклона между собой. И индексы этих линий
        можно удалить из списка, так как по условию задачи углы наклона между разными линиями в кластере должны
        сильно различаться
        """
        working_area_shape: List[int] = self.get_working_area_shape()

        for i in range(working_area_shape[0]):
            for j in range(working_area_shape[1]):
                lines: List[Line] = self.squares[i][j].lines

                # Отсортируем линии по возрастанию углов наклона
                lines = sorted(lines, key=lambda x: x.angle)

                # Удалим линии, у которых слишком маленькое различие по углу наклона
                filtered_lines: List[Line] = []
                line_count: int = len(lines)
                for k in range(line_count - 1):
                    angle_tangent_difference: float = lines[k].angle - lines[k + 1].angle
                    # todo: Убедиться что угол взят правильно и это условие верное
                    if abs(angle_tangent_difference) > 0.0001:
                        filtered_lines.append(lines[k])

                self.squares[i][j].lines = filtered_lines

    def calculate_lines_for_all_squares(self):
        """
        Для каждого квадрата сетки подсчитывает индексы линий, которые через него проходят
        """
        for i, line in enumerate(self.lines):
            first_point: List[float] = [line.first_point.x, line.first_point.y]
            second_point: List[float] = [line.second_point.x, line.second_point.y]
            line_coordinates: List[List[int]] = geometry.get_line_coordinates(
                first_point,
                second_point,
                self.working_area_limits
            )
            # todo: Убедиться что точность не потеряна
            for point in line_coordinates:
                x: int = int(round(point[0])) + abs(self.working_area_limits[0])
                y: int = int(round(point[1])) + abs(self.working_area_limits[2])
                self.squares[x][y].lines.append(self.lines[i])

    def get_image_with_lines(self):
        """
        Нарисовать линии на двумерной бинарной матрице
        """
        array_shape: Tuple[int, int] = (
            abs(self.working_area_limits[1] - self.working_area_limits[0]),
            abs(self.working_area_limits[2] - self.working_area_limits[3])
        )

        image: np.ndarray = np.zeros(array_shape, dtype=np.int16)
        for line in self.lines:
            first_point: List[float] = [line.first_point.x, line.first_point.y]
            second_point: List[float] = [line.second_point.x, line.second_point.y]
            line_coordinates: List[List[int]] = geometry.get_line_coordinates(
                first_point,
                second_point,
                self.working_area_limits
            )
            for point in line_coordinates:
                x: int = int(round(point[0]))
                y: int = int(round(point[1]))
                image[x + abs(self.working_area_limits[0]), y + abs(self.working_area_limits[2])] = 1
        return image

    def get_line_intersection_map(self):
        """
        Получить карту пересечений линий в каждой точке рабочей области
        """
        working_area_shape: List[int] = self.get_working_area_shape()
        image: np.ndarray = np.zeros(working_area_shape, dtype=np.int32)

        for i in range(working_area_shape[0]):
            for j in range(working_area_shape[1]):
                lines: List[Line] = self.squares[i][j].lines
                line_count: int = len(lines)
                image[i, j] = line_count

        return image
