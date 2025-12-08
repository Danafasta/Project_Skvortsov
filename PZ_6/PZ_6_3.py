# Дан список размера N, все элементы которого, кроме одного, упорядочены по убыванию. Сделать список упорядоченным, переместив элемент, нарушающий упорядоченность, на новую позицию.

import random

try:
    n = int(input("Введите размер списка N: "))
    a = []
    for i in range(n):
        a.append(n - i)

    bad_pos = random.randint(0, n - 1)
    a[bad_pos] = random.randint(1, n + 10)
    print("Исходный список:", a)

    bad_index = 0
    for i in range(1, n):
        if a[i] > a[i - 1]:
            bad_index = i
            break

    x = a.pop(bad_index)

    new_index = len(a)
    for i in range(len(a)):
        if x >= a[i]:
            new_index = i
            break

    a.insert(new_index, x)
    print("Упорядоченный список:", a)

except:
    print("Ошибка ввода данных.")