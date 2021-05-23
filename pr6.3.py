class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


user_worker = Position(input('Введите имя: '), input('Введите фамилию: '), input('Введите должность: '),
                       int(input('Введите ежемесячный оклад: ')), int(input('Введите ежемесячную премию: ')))
print(f'Сотрудник {user_worker.get_full_name()} с доходом {user_worker.get_total_income()} в месяц')
