from typing import List
from matplotlib import pyplot as plt
import numpy as np
from working_area import WorkingArea
import read_write as rw
from line import Line


def print_lines(lines: List[Line]):
    """
    Напечатать информацию о линиях в консоль
    """
    for i, line in enumerate(lines):
        print(f'Линия {i}: ')
        line.print_line_points()
        print()


def rescale_line_points(lines: List[Line], rescale_value: float) -> List[Line]:
    """
    Делит все точки массива с координатами линий на заданное значение для изменения масштаба

    :param lines: Список линий
    :param rescale_value: Значение, на которое будут поделены все координаты точек
    """
    line_count: int = len(lines)
    for i in range(line_count):
        lines[i].first_point.x /= rescale_value
        lines[i].first_point.y /= rescale_value
        lines[i].second_point.x /= rescale_value
        lines[i].second_point.y /= rescale_value
    return lines


def main():
    cluster_count: int
    lines: List
    lines, cluster_count = rw.read_file_with_line_points(file_index=2)

    # Вывод отладочной информации
    line_count: int = len(lines)
    print(f'Количество входных линий: {line_count}')
    print(f'Количество кластеров: {cluster_count}')

    # Уменьшим масштаб точек, задающих линии
    lines = rescale_line_points(lines, 100.0)

    # Отобразим картинку со всеми прямыми
    working_area_limits: List[int] = [-100, 100, -100, 100]
    working_area: WorkingArea = WorkingArea(lines, working_area_limits)
    image = working_area.get_line_intersection_map()

    # Отсечём по порогу самые яркие точки
    # image = np.where(image > 100, 1, 0)

    plt.imshow(image, interpolation='none')
    pass


if __name__ == '__main__':
    main()
