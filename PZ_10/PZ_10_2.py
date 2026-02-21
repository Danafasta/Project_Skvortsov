#Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое
#количество символов в тексте. Сформировать новый файл, в который поместить строку наибольшей длины

f = open("text18-20.txt", "r", encoding="UTF-16 LE")
text = f.read()
f.close()

print("Содержимое файла: ")
print(text)

count = len(text)
print(f"Количество символов в тексте: {count}")

lines = text.splitlines()
longest_line = max(lines, key=len)

f1 = open("new_text.txt", "w", encoding="UTF-8")
f1.write(longest_line)
f1.close()

print(f"Самая длинная строка записана в new_text.txt")