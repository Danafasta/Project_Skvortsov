# Практическое занятие №14. Вариант 20. Задание 2. Дано целое положительное число. Вывести символы, изображающие цифры этого числа (в порядке слева направо).
from tkinter import *

def solve(event):
    val = entry.get()
    if val.isdigit() and int(val) > 0:
        label_res.config(text=" ".join(val))
    else:
        label_res.config(text="Ошибка! Введите целое положительное число.")

root = Tk()
root.geometry("300x200")

Label(root, text="Введите число:").pack(pady=20)
entry = Entry(root, width=20)
entry.pack()

btn = Button(root, text="Вывести цифры", width=20)
btn.pack(pady=20)
btn.bind("<Button-1>", solve)

label_res = Label(root, text="", width=30)
label_res.pack(pady=10)

root.mainloop()