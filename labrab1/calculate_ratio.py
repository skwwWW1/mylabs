#!/usr/bin/env python3
import sys
import random

import sys
import random


print("Введите число:")
try:
    user_input = float(input())
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите числовое значение.")
    exit(1)
random_number = random.randint(-10, 10)
if random_number == 0:
    print("Случайно было выбрано число 0. Деление на ноль невозможно.")
    exit(2)
try:
    division_result = user_input / random_number
    print(division_result)
except ZeroDivisionError as e:
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Ошибка в calculate_ratio.py: {e}\n")
