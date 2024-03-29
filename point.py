class Point:
    """
    Класс для работы с точкой

    Аттрибуты:
        x: Координата x точки
        y: Координата y точки
    """
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y