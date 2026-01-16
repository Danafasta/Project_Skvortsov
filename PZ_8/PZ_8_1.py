#Подсчитайте сумму значений в словаре. d = {'a':100, 'b':200}.

d = {'a': 100, 'b': 200}
try:
    s = sum(d.values())
    print("Сумма значений в словаре:", s)
except Exception as e:
    print("Ошибка:", e)