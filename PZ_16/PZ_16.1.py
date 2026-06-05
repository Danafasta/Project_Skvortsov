#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для инкремента и декремента значения.


class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self, step=1):
        self.value += step

    def decrement(self, step=1):
        self.value -= step


c1 = Counter(10)
c1.increment(5)
c1.decrement(3)
print(f"Значение счетчика: {c1.value}")