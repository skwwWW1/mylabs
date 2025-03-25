#!/usr/bin/env python3

import sys
import math

def main():
    try:
        data = sys.stdin.read().strip()
        C = float(data)
        if C < 0:
            raise Exception("���������� ��������� ���������� ������ �� �������������� �����.")
    except ValueError:
        print("������� �������� ������", file=sys.stderr)
        with open("errors.txt", "a") as error_file:
            error_file.write("������ � calculate_sqrt.py: �������� ����\n")
        return
    except EOFError:
        print("������ �� ���������", file=sys.stderr)
        with open("errors.txt", "a") as error_file:
            error_file.write("������ � calculate_sqrt.py: ������ �� ���������\n")
        return
    except Exception as e:
        with open("errors.txt", "a") as error_file:
            error_file.write(f"������ � calculate_sqrt.py: {e}\n")
        return
    else:
        res = math.sqrt(C)
        with open("output.txt", "w") as output_file:
            output_file.write(f"���������� ������: {res}\n")
    return

if __name__ == "__main__":
    main()