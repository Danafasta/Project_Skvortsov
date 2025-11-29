"Составить функцию, которая напечатает сорок любых символов."

def print_forty_chars():
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    result = ""
    for i in range(40):
        index = i % len(symbols)  
        result += symbols[index]
    print(result)

try:
    print("Сорок любых символов:")
    print_forty_chars()
except Exception as e:
    print(f"Произошла ошибка: {e}")