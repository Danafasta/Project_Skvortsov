
#Создание базового класса "Работник" и его наследование для создания классов "Менеджер" и "Инженер".
# В классе "Работник" будут общие методы, такие как "работать" и "получать зарплату", а классы-наследники будут иметь свои уникальные методы и свойства, такие как "управлять командой" и "проектировать системы".

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} выполняет свои рабочие обязанности."

    def receive_salary(self) -> str:
        return f"{self.name} получил зарплату в размере {self.salary:.2f} руб."


class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int) -> None:
        super().__init__(name, salary)
        self.team_size = team_size

    def manage_team(self) -> str:
        return f"{self.name} управляет командой из {self.team_size} человек."


class Engineer(Employee):
    def __init__(self, name: str, salary: float, specialization: str) -> None:
        super().__init__(name, salary)
        self.specialization = specialization

    def design_systems(self) -> str:
        return f"{self.name} проектирует системы в области: {self.specialization}."


if __name__ == "__main__":
    worker = Employee("Иван Иванов", 50000.0)
    manager = Manager("Анна Петрова", 95000.0, 8)
    engineer = Engineer("Сергей Сидоров", 85000.0, "Backend-разработка")

    print(worker.work())
    print(worker.receive_salary())
    print(manager.work())
    print(manager.manage_team())
    print(manager.receive_salary())
    print(engineer.work())
    print(engineer.design_systems())
    print(engineer.receive_salary())

    staff = [worker, manager, engineer]
    
    names = list(map(lambda emp: emp.name, staff))
    print(f"Список сотрудников: {names}")
    
    high_earners = list(filter(lambda emp: emp.salary > 80000, staff))
    high_earners_names = [emp.name for emp in high_earners]
    print(f"Сотрудники с зарплатой выше 80000: {high_earners_names}")