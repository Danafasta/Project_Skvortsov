#В последовательности на n целых элементов в первой ее половине найти количество положительных элементов.

from functools import reduce

L = [1, -5, 3, 4, -2, 6, 7, -8, 9, 10]
n = len(L)

first_half = L[:n // 2]

count = reduce(lambda x, y: x + y, map(lambda x: 1, filter(lambda x: x > 0, first_half)), 0)

print(count)