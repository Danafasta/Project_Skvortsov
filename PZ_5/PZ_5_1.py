"Составить функцию, которая напечатает сорок любых символов."

import random

def print_forty_chars():
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    result = ""
    for _ in range(40):
        result += random.choice(symbols)
    print(result)

try:
    print("Сорок любых символов:")
    print_forty_chars()
except Exception as e:
    print(f"Произошла ошибка: {e}")