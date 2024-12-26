#!/usr/bin/env python3
import sys
import os

class ValidationError(Exception):
    pass

def validate_name(name):
    if not name[0].isupper():
        raise ValidationError("Имя не начинается с заглавной буквы.")
    if not name.isalpha():
        raise ValidationError("Имя содержит недопустимые символы (разрешены только буквы).")

def greet(name):
    print(f"Привет, {name}!")

def greet_from_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                name = line.strip()
                try:
                    validate_name(name)
                    greet(name)
                except ValidationError as e:
                    with open("error.txt", "a") as error_file:
                        error_file.write(f"Неверное имя '{name}': {e}\n")
    except FileNotFoundError:
        sys.stderr.write(f"Ошибка: Файл '{filename}' не найдено.\n")
        return
    except Exception as e:
        sys.stderr.write(f"Ошибка в greet_from_file: {e}\n")
        return

def interactive_greeting():
    while True:
        try:
            name = input("Пожалуйста, введите свое имя: ").strip()
            try:
                validate_name(name)
                greet(name)
            except ValidationError as e:
                with open("error.txt", "a") as error_file:
                    error_file.write(f"Неверное имя '{name}': {e}\n")
                continue
        except KeyboardInterrupt:
            print("\nДо свидания!")
            sys.exit(0)
        except Exception as e:
            sys.stderr.write(f"Неожиданная ошибка: {e}\n")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if os.path.isfile(filename):
            greet_from_file(filename)
        else:
            sys.stderr.write(f"Ошибка: '{filename}' недопустимый файл.\n")
    else:
        interactive_greeting()
