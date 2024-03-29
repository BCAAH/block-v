from typing import List, Tuple
from line import Line
from point import Point


def read_file_with_line_points(file_index: int = 0) -> Tuple[List[Line], int]:
    """
    Прочитать входные координаты линий из файла

    :param file_index: Индекс входного файла
    :return:
    1) Линии
    2) Количество кластеров
    """
    with open(f'test_files/{file_index}-lines.txt') as f:
        # Чтение входного файла с прямыми
        file_strings: List[str] = f.readlines()

        # Чтение первой строки файла
        splitted_first_file_line: List[str] = file_strings[0].split(' ')
        line_count: int = int(splitted_first_file_line[0])
        cluster_count: int = int(splitted_first_file_line[1])

        # Чтение остальных строк с координатами прямых
        lines: List[Line] = []
        for i in range(line_count):
            splitted_file_line: List[str] = file_strings[i + 1].split(' ')
            line_coordinates: List[float] = list(map(float, splitted_file_line))
            first_point: Point = Point(line_coordinates[0], line_coordinates[1])
            second_point: Point = Point(line_coordinates[2], line_coordinates[3])
            line = Line(first_point, second_point)
            lines.append(line)

        return lines, cluster_count
