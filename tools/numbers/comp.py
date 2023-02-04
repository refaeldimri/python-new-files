import os
from files.tools.numbers.simp import Simp


def sum_of_digits(number):
    permission_error = str(os.getenv("PERMISSION_ERROR"))
    if not Simp.flag:
        raise PermissionError(permission_error)
    sum_digits = 0
    while number != 0:
        sum_digits += number % 10
        number = number // 10
    return sum_digits


def ispl(number):
    permission_error = str(os.getenv("PERMISSION_ERROR"))
    value_error = os.getenv("VALUE_ERROR")
    if not Simp.flag:
        raise PermissionError(permission_error)
    if not isinstance(number, int):
        raise ValueError(value_error)
    else:
        return str(number) == str(number)[::-1]

