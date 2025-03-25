#!/usr/bin/env python3

import sys
import random

def main():
    try:
        print("Введите число:")
        data = input()
        A = float(data)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите числовое значение.", file=sys.stderr)
        return
    B = random.randint(-10, 10)
    if B == 0:
        print("Случайно было выбрано число 0. Деление на ноль невозможно.", file=sys.stderr)
        return
    try:
        res = A / B
    except ZeroDivisionError:
        with open("errors.txt", "a") as error_file:
            error_file.write("Ошибка в calculate_ratio.py: деление на ноль\n")
    else:
        print(res)
    return

if __name__ == "__main__":
    main()