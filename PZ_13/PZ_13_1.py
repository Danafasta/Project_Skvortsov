import re

with open("writer.txt", "r", encoding="utf-8") as file:
    text = file.read()

lines = text.splitlines()
surname_re = re.compile(r"^([А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)*)")
year_re = re.compile(r"\(\d{4}-\d{4}\)")

surnames = []
for line in lines:
    m = surname_re.match(line.strip())
    if m and year_re.search(line):
        surnames.append(m.group(1))

print(len(surnames))

new_text = re.sub(r"\bроман\b", "произведение", text, flags=re.IGNORECASE)

with open("writer_replaced.txt", "w", encoding="utf-8") as file:
    file.write(new_text)