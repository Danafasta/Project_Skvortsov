##Проверить истинность высказывания: "Срдеи трех данны целых чисел есть хотя бы одна пара взаимно противоположных.

a, b, c = int(input("Введите первое число: ")), input("Введите второе число: "), input("Введите третье число: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = int("Введите первое число")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = int("Введите первое число")

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели!")
        c = int("Введите третье  число")

if a == -b or a == -c or b == -a or b == -c:
    print("Среди этих чисел есть пара взаимо противоположных")
else:
    print("Среди этих чисел нет взаимообратных")
        