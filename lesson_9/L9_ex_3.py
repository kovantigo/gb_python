class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

work = Position('Ivan', 'Ivanov', 'driver', 100000, 10000)
print(work.get_total_income())
print(work.get_full_name())
print(work.position)
print(work._income['wage'])
