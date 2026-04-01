#В матрице найти сумму элементов первых двух строк.

import random

rows = 5
cols = 5

matrix = [[random.randint(-10, 10) for i in range(cols)] for j in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

sum_first_two = sum(matrix[0]) + sum(matrix[1])
print(f"Сумма элементов первых двух строк: {sum_first_two}")