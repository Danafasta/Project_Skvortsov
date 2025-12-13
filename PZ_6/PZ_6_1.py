# Дан список размера N и целые числа K и L (1 < K < L < N). Найти среднее арифметическое элементов списка с номерами от K до L включительно.

import random

try:
    N = int(input("Введите размер списка N: "))
    K = int(input("Введите K: "))
    L = int(input("Введите L: "))
    if not (1 < K < L < N):
        print("Ошибка: должно выполняться 1 < K < L < N")
    else:
        a = []
        for i in range(N):
            a.append(random.randint(0, 100))
        print("Список:", a)
        s = 0
        for i in range(K - 1, L):
            s += a[i]
        sr = s / (L - K + 1)
        print("Среднее арифметическое:", sr)
except:
    print("Ошибка ввода данных.")