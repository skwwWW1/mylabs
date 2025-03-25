#!/usr/bin/env python3

import sys
import random

def main():
    try:
        A = random.randint(-10, 10)
        print(A)
        B = 100 / A
    except ZeroDivisionError:
        print("Деление на 0", file=sys.stderr)
        with open("errors.txt", "a") as error_file:
            error_file.write("Ошибка в generate_number.py: деление на ноль\n")
        return
    except Exception as e:
        with open("errors.txt", "a") as error_file:
            error_file.write(f"Ошибка в generate_number.py: {e}\n")
        return
    else:
        print(B)
    return

if __name__ == "__main__":
    main()