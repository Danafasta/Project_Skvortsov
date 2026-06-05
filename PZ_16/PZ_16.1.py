#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для инкремента и декремента значения

class Counter:
    def __init__(self, initial_value: int = 0) -> None:
        self.current_value = initial_value

    def increment(self, step: int = 1) -> None:
        if step > 0:
            self.current_value += step

    def decrement(self, step: int = 1) -> None:
        if step > 0:
            self.current_value -= step


if __name__ == "__main__":
    counter1 = Counter(10)
    counter1.increment(5)
    counter1.decrement(3)
    print(f"Значение счетчика 1: {counter1.current_value}")

    counter2 = Counter(0)
    counter2.increment(20)
    print(f"Значение счетчика 2: {counter2.current_value}")

    counters = [counter1, counter2]
    values = list(map(lambda c: c.current_value, counters))
    print(f"Список значений всех счетчиков: {values}")