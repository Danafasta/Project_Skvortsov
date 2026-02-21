#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. 
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Числа кратные трем:
#Количество чисел кратных трем:

import random

chars = [random.randint(-10, 10) for i in range(10)]

f = open("file.txt", "w", encoding="UTF-8")
f.write(" ".join(map(str, chars)))
f.close()

# Чтение из файла
f_read = open("file.txt", "r", encoding="UTF-8")
data = f_read.read().split()
f_read.close()

numbers = [int(x) for x in data]

# Обработка
count = len(numbers)
min_num = min(numbers)
div_by_3 = [x for x in numbers if x % 3 == 0]
count_div_by_3 = len(div_by_3)

# Запись результата
f3 = open("new_file.txt", "w", encoding="UTF-8")
f3.write(f"Исходные данные: {' '.join(map(str, numbers))}\n")
f3.write(f"Количество элементов: {count}\n")
f3.write(f"Минимальный элемент: {min_num}\n")
f3.write(f"Числа кратные трем: {' '.join(map(str, div_by_3))}\n")
f3.write(f"Количество чисел кратных трем: {count_div_by_3}")
f3.close()