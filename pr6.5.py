class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        Stationary.__init__(self, title)

    def draw(self):
        return f'Запуск отрисовки. Выбрано: {self.title}'


class Pencil(Stationary):
    def __init__(self, title):
        Stationary.__init__(self, title)

    def draw(self):
        return f'Запуск отрисовки. Выбрано: {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        Stationary.__init__(self, title)

    def draw(self):
        return f'Запуск отрисовки. Выбрано: {self.title}'


user_pen = Pen('Ручка')
user_pencil = Pencil('Карандаш')
user_handle = Handle('Маркер')

print(user_pen.draw())
print(user_pencil.draw())
print(user_handle.draw())