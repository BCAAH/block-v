from typing import List, Union
import numpy as np
import utils


def get_line_coordinates(
        first_point: Union[np.ndarray, List[Union[float, int]]],
        second_point: Union[np.ndarray, List[Union[float, int]]],
        working_area_limits: List[int],
        point_count: int = -1,
        round_coordinates: bool = True
) -> List[List[Union[float, int]]]:
    """
    Получить список координат линии в трёхмерном пространстве

    :param first_point: Координаты x, y первой точки линии
    :param second_point: Координаты x, y второй точки линии
    :param working_area_limits: Пределы рабочей области - минимальные и максимальные значения по x и по y
    :param point_count: Количество точек в прямой. Если -1, значит будет определено автоматически
    :param round_coordinates: Флаг, показывающий, нужно ли использовать округление координат выходной линии
    """
    x1: float = first_point[0]
    y1: float = first_point[1]
    x2: float = second_point[0]
    y2: float = second_point[1]
    if round_coordinates:
        x1 = int(round(x1))
        y1 = int(round(y1))
        x2 = int(round(x2))
        y2 = int(round(y2))

    cathetus_x: float = abs(x1 - x2)
    cathetus_y: float = abs(y1 - y2)
    line_coordinates: List[List[Union[float, int]]] = []
    step: float = 1.0
    array_shape: List[int] = [
        abs(working_area_limits[1] - working_area_limits[0]),
        abs(working_area_limits[2] - working_area_limits[3])
    ]

    if cathetus_x >= cathetus_y:
        if point_count > 0:
            step = array_shape[0] / point_count
        else:
            point_count = array_shape[0]
        x: float = working_area_limits[0]
        for i in range(working_area_limits[0], point_count):
            y: float = (y2 - y1) * (x - x1) / utils.get_small_value_if_zero((x2 - x1)) + y1
            if (working_area_limits[0] <= x <= working_area_limits[1] - 1)\
                    and (working_area_limits[2] <= y <= working_area_limits[3] - 1):
                point: List[Union[float, int]]
                if round_coordinates:
                    point = [np.round(x).astype(np.int32), np.round(y).astype(np.int32)]
                else:
                    point = [x, y]
                line_coordinates.append(point)
            x += step
    else:
        if point_count > 0:
            step = array_shape[1] / point_count
        else:
            point_count = array_shape[1]
        y: float = working_area_limits[2]
        for i in range(working_area_limits[2], point_count):
            x: float = (x2 - x1) * (y - y1) / utils.get_small_value_if_zero((y2 - y1)) + x1
            if (working_area_limits[0] <= x <= working_area_limits[1] - 1)\
                    and (working_area_limits[2] <= y <= working_area_limits[3] - 1):
                point: List[Union[float, int]]
                if round_coordinates:
                    point = [np.round(x).astype(np.int32), np.round(y).astype(np.int32)]
                else:
                    point = [x, y]
                line_coordinates.append(point)
            y += step
    if len(line_coordinates) < 2:
        line_coordinates = [list(first_point), list(second_point)]
    return line_coordinates
