line = "Петров Иван ПОКС-29 5 4 3 2 5 4 5 4"
parts = line.split()
student = {
    'Фамилия': parts[0],
    'Имя': parts[1],
    'Группа': parts[2],
    'Оценки': []
}
for i in range(3, len(parts)):
    student['Оценки'].append(int(parts[i]))
avg = sum(student['Оценки']) / len(student['Оценки'])
print(avg)