#!/usr/bin/env python3
import sys
import math

try:

    number = float(sys.stdin.read().strip())

    if number < 0:
        raise ValueError("Невозможно вычислить квадратный корень из отрицательного числа.")
    result = math.sqrt(number)
    with open("output.txt", "w") as output_file:
        output_file.write(f"Квадратный корень: {result}\n")
except Exception as e:
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Ошибка в calculate_sqrt.py: {e}\n")
