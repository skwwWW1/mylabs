#!/usr/bin/env python3
import sys
import random

import random
try:
    A = random.randint(-10, 10)
    print(A)
    B = 100 / A
    print(B)
except Exception as e:
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Ошибка в generate_number.py: {e}\n")
