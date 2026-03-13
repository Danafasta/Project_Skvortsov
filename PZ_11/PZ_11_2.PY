#Из заданной строки отобразить только символы нижнего регистра. 
#Использовать библиотеку string. Строка'In PyCharm, you can specify third-party standalone applications and run them as External Tools'.
from string import ascii_lowercase

text = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

result = [char for char in text if char in ascii_lowercase]
print(''.join(result))