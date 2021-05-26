class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return round(self.width / 6.5 + 0.5, 2)

    def get_square_jacket(self):
        return round(self.height * 2 + 0.3, 2)

    @property
    def get_square_total(self):
        return str(f'Требуется ткани: {round(self.width / 6.5 + 0.5, 2) + round(self.height * 2 + 0.3, 2)}')


class Coat(Textil):
    def __init__(self, width, height):
        Textil.__init__(self, width, height)
        self.square_coat = round(self.width / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Треебуется ткани на пальто: {self.square_coat}'


class Jacket(Textil):
    def __init__(self, width, height):
        Textil.__init__(self, width, height)
        self.square_jacket = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Треебуется ткани на пиджак: {self.square_jacket}'

coat = Coat(5, 10)
jacket = Jacket(6, 12)
print(coat)
print(jacket)
print(coat.get_square_total)
print(jacket.get_square_total)
print(jacket.get_square_coat())
print(jacket.get_square_jacket())