"""
дано вещественное число x и целое число n (> 0). 
найти значение выражения:
1 - x^2/(2!) + x^4/(4!) - ... + (-1)^n * x^(2n)/((2n)!)
(n! = 1 * 2 * ... * n)
полученное число является приближенным значением функции cos в точке x.
"""

while True:
    try:
        x = float(input("Введите X: "))
        break
    except ValueError:
        print("Неправильно ввели X!")

while True:
    try:
        n = int(input("Введите N (>0): "))
        if n > 0:
            break
        else:
            print("N должно быть больше 0!")
    except ValueError:
        print("Неправильно ввели N!")

total = 0
k = 0
while k <= n:
    sign = 1 if k % 2 == 0 else -1

    power = 1
    i = 0
    while i < 2 * k:
        power *= x
        i += 1

    factorial = 1
    i = 1
    while i <= 2 * k:
        factorial *= i
        i += 1

    total += sign * power / factorial
    k += 1

print(f"Приближенное значение cos({x}) = {total}")