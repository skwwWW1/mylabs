#!/usr/bin/env python3

import sys
import math

def main():
    try:
        data = sys.stdin.read().strip()
        C = float(data)
        if C < 0:
            raise Exception("Невозможно вычислить квадратный корень из отрицательного числа.")
    except ValueError:
        print("Введены неверные данные", file=sys.stderr)
        with open("errors.txt", "a") as error_file:
            error_file.write("Ошибка в calculate_sqrt.py: неверный ввод\n")
        return
    except EOFError:
        print("Данные не поступили", file=sys.stderr)
        with open("errors.txt", "a") as error_file:
            error_file.write("Ошибка в calculate_sqrt.py: данные не поступили\n")
        return
    except Exception as e:
        with open("errors.txt", "a") as error_file:
            error_file.write(f"Ошибка в calculate_sqrt.py: {e}\n")
        return
    else:
        res = math.sqrt(C)
        with open("output.txt", "w") as output_file:
            output_file.write(f"Квадратный корень: {res}\n")
    return

if __name__ == "__main__":
    main()