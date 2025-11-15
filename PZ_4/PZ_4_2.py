"""Дано целое число (N>0) Найти сумму 1^1 + 2^2 + ... N^n"""

while True:
    try:
        n = int(input("Введите положительное целое число N: "))
        if n <= 0:
            print("Число должно быть больше 0. Попробуйте снова.")
            continue

        total = 0
        i = 1
        while i <= n:
            total += i ** i
            i += 1

        print(f"Сумма 1^1 + 2^2 + ... + {n}^{n} = {total}")
        break
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")