class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, weight, thickness):
        try:
            return self._length * self._width * int(weight) * int(thickness)
        except ValueError:
            print('Ошибка!')


a = Road(5, 2)
print(a.calculate_mass(input('Введите массу асфальта для покрытия 1 кв.м дороги асфальтом, толщиной в 1 см: '),
                       input('Введите числом толщину полотна: ')))
