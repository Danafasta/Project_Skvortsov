#В матрице найти минимальный и максимальные элементы.


import random

rows = 5
cols = 5

matrix = [[random.randint(-10, 10) for i in range(cols)] for i in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

all_elements = [element for row in matrix for element in row]
min_element = min(all_elements)
max_element = max(all_elements)

print(f"Минимальный элемент: {min_element}")
print(f"Максимальный элемент: {max_element}")
