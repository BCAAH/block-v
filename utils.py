from typing import Union


def get_small_value_if_zero(
        value: Union[float, int],
        small_value: float = 0.01,
        very_small_value: float = 0.000001
) -> Union[float, int]:
    """
    Вернуть близкое к нулю значение если на входе значение = 0. Если на входе будет отрицательное очень маленькое
    значение, то на выходе тоже будет отрицательное маленькое число, но не такое маленькое, которое было на входе.
    Если же входное значение не является близким к нулю, то оно возвращено и будет

    :param: value: Исходное значение
    :param: small_value: Маленьное число, которое будет возхвращено, если входное значение меньше очень маленького числа
    Знак будет взят от входного значения
    :param: very_small_value: Очень маленьное число
    """
    if value > 0:
        if value < very_small_value:
            return small_value
        else:
            return value
    else:
        if abs(value) < very_small_value:
            return small_value
        else:
            return value
