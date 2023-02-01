from files.tools.numbers.simp import Simp


def sum_of_digits(number):
    if not Simp.flag:
        return "You Can not use this function before you use " \
               "at least one simp class's function"
    sum_digits = 0
    while number != 0:
        sum_digits += number % 10
        number = number // 10
    return sum_digits


def ispl(number):
    if not Simp.flag:
        return "You Can not use this function before you use at least one simp class's function"
    if not isinstance(number, int):
        raise ValueError("invalid input")
    else:
        return str(number) == str(number)[::-1]

