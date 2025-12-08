# Дан целочисленный список размера N. Найти максимальное количество его одинаковых элементов.

import random

try:
    n = int(input("Введите размер списка N: "))
    a = []
    for i in range(n):
        a.append(random.randint(1, 10))
    print("Список:", a)
    max_count = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if a[j] == a[i]:
                count += 1
        if count > max_count:
            max_count = count
    print("Максимальное количество одинаковых элементов:", max_count)
except:
    print("Ошибка ввода данных.")