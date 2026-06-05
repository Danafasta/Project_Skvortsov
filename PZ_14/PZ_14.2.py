#Дано целое положительное число. Вывести символы, изображающие цифры этого числа (в порядке слева направо).
from tkinter import *

def solve(event):
    val = entry.get()
    if val.isdigit() and int(val) > 0:
        label_res.config(text=" ".join(val))
    else:
        label_res.config(text="Ошибка! Введите целое положительное число.")

root = Tk()
root.title("Вывод цифр")
root.geometry("420x200")

Label(root, text="Введите число:").pack(pady=15)
entry = Entry(root, width=25)
entry.pack()

btn = Button(root, text="Вывести цифры", width=20)
btn.pack(pady=15)
btn.bind("<Button-1>", solve)

label_res = Label(root, text="")
label_res.pack(pady=10)

root.mainloop()
