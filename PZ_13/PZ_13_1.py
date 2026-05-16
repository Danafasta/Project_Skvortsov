# Вариант 20. Из текстового файла(writer.txt) выбрать фамилии писателей, посчитать количество фамилий.
# Создать новый файл, в котором выполнить замену слова «роман» на слово «произведение».

import re

with open("writer.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
last_name = re.compile(r"^([А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)*)")
year = re.compile(r"\(\s*\d{4}\s*-\s*\d{4}\s*\)")

surnames = [m.group(1) for line in lines 
            if (m := last_name.match(line.strip())) and year.search(line)]

print(len(surnames))

new_text = re.sub(r"\bроман\b", "произведение", text, flags=re.IGNORECASE)

with open("writer_replaced.txt", "w", encoding="utf-8") as f:
    f.write(new_text)