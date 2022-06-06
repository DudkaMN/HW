class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus};


class Position(Worker):
    def get_full_name(self):
        print(f'Full name: {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Total income: {sum(self.__income.values())}')


worker_1 = Position('Ivan', 'Kolos', 'Tech', 100, 50)
worker_2 = Position('Sergey', 'Ivanov', 'Dir', 200, 40)
worker_3 = Position('Irina', 'Lalina', 'Man', 150, 50)
worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()
worker_3.get_full_name()
worker_3.get_total_income()
