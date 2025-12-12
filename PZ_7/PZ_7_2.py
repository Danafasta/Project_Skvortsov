# Дана строка, состоящая из русских слов, набранных заглавными буквами и разделённых пробелами. Преобразовать каждое слово в строке, заменив в нём все последующие вхождения его первой буквы на символ «.» (точка). Количество пробелов между словами не изменять.

try:
    s = input("Введите строку: ")
    words = s.split(' ')
    result = []
    for word in words:
        if word:
            first = word[0]
            new_word = first + word[1:].replace(first, '.')
            result.append(new_word)
        else:
            result.append(word)
    print(' '.join(result))
except:
    print("Ошибка")