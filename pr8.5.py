class StoreHardware:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def get_info(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Hardware:
    def __init__(self, name, print_volume, year):
        self.name = name
        self.print_volume = print_volume
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'производитель {self.name}: объем {self.print_volume}; год выпуска{self.year}'


class Printer(Hardware):
    def __init__(self, series, name, print_volume, year):
        Hardware.__init__(self, name, print_volume, year)
        self.series = series

    def __repr__(self):
        return f'производитель {self.name}: модель {self.series}; объем {self.print_volume}; год выпуска {self.year}'

    def action_print(self):
        return 'Печатает'


class Scaner(Hardware):
    def __init__(self,series, name, print_volume, year):
        Hardware.__init__(self, name, print_volume, year)
        self.series = series

    def __repr__(self):
        return f'производитель {self.name}: модель {self.series}; объем {self.print_volume}; год выпуска {self.year}'

    def action_print(self):
        return 'Сканирует'


class Xerox(Hardware):
    def __init__(self,series, name, print_volume, year):
        Hardware.__init__(self, name, print_volume, year)
        self.series = series

    def __repr__(self):
        return f'производитель {self.name}: модель {self.series}; объем {self.print_volume}; год выпуска {self.year}'

    def action_print(self):
        return 'Копирует'


store= StoreHardware()
scaner = Scaner('scanjet', 'hp', 321, 2020)
store.add_to(scaner)
scaner = Scaner('LIDE300','canon', 311, 2019)
store.add_to(scaner)
printer = Printer('e-320', 'sony', 126, 2018)
store.add_to(printer)
print(store._dict)
store.get_info('Scaner')
print(store._dict)