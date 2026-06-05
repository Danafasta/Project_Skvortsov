# Создание базового класса "Работник" и его наследование для создания классов "Менеджер" и "Инженер".
# В классе "Работник" будут общие методы, такие как "работать" и "получать зарплату", а классы-наследники будут иметь свои уникальные методы и свойства, 
# такие как "управлять командой" и "проектировать системы".

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} работает."

    def receive_salary(self):
        return f"{self.name} получил {self.salary} руб."


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def manage_team(self):
        return f"{self.name} управляет командой из {self.team_size} человек."


class Engineer(Employee):
    def __init__(self, name, salary, specialization):
        super().__init__(name, salary)
        self.specialization = specialization

    def design_systems(self):
        return f"{self.name} проектирует системы ({self.specialization})."


worker = Employee("Иван", 50000)
manager = Manager("Анна", 90000, 5)
engineer = Engineer("Сергей", 80000, "Backend")

print(worker.work(), worker.receive_salary())
print(manager.work(), manager.manage_team(), manager.receive_salary())
print(engineer.work(), engineer.design_systems(), engineer.receive_salary())