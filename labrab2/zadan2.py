#!/usr/bin/python3

import sys
import os

def is_valid_name(s):
    if not s or not s[0].isupper():
        return False, "Name does not start with a capital letter."
    if not all(c.isalpha() for c in s):
        return False, "Name contains invalid characters (only letters are allowed)."
    return True, ""

def print_greeting(n):
    print(f"Добрый день, {n}!")

def handle_file(filepath):
    if not os.path.isfile(filepath):
        print(f"Ошибка: '{filepath}' не является файлом", file=sys.stderr)
        return
    with open(filepath, "r") as source:
        for item in source:
            name = item.strip()
            valid, error = is_valid_name(name)
            if valid:
                print_greeting(name)
            else:
                with open("errors.log", "a") as err_log:
                    err_log.write(f"Invalid name '{name}': {error}\n")

def process_input():
    print("Введите имена (для завершения нажмите Ctrl+D):")
    while True:
        try:
            entry = input("Имя: ").strip()
            valid, error = is_valid_name(entry)
            if valid:
                print_greeting(entry)
            else:
                with open("errors.log", "a") as err_log:
                    err_log.write(f"Invalid name '{entry}': {error}\n")
        except EOFError:
            print("\nПрограмма завершена.")
            break
        except KeyboardInterrupt:
            print("\nДо новых встреч!")
            break

def main():
    if len(sys.argv) == 2:
        handle_file(sys.argv[1])
    else:
        process_input()
    return

if __name__ == "__main__":
    main()