from time import sleep
from random import randint

class Car:

    def __init__(self, color, name, is_polise):
        self.speed = randint(20, 180)
        self.color = color
        self.name = name
        self.is_police = is_polise

    def go(self):
        print(f'Машина {self.name}, цвет {self.color}, поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась\n')
        print('-' * 30)

    def show_speed(self):
        print(f'Машина {self.name} едет со скоротью {self.speed}')

    def turn(self):
        i = 0
        self.go()
        self.show_speed()
        while i < 3:
            if i == 0:
                print(f'Машина {self.name} повернула налево')
                sleep(2)
            elif i == 1:
                print(f'Машина {self.name} повернула направо')
                sleep(2)
            i += 1
        self.stop()

class TownCar(Car):

    def __init__(self, color, name, is_polise = False):
        Car.__init__(self, color, name, is_polise)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости! Скорость {self.speed} выше допустимой')
        else:
            print(f'Машина {self.name} едет со скоротью {self.speed}')

class SportCar(Car):

    def __init__(self, color, name, is_polise = False):
        Car.__init__(self, color, name, is_polise)

class WorkCar(Car):

    def __init__(self, color, name, is_polise = False):
        Car.__init__(self, color, name, is_polise)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Машина {self.name} едет со скоротью {self.speed}')

class PoliceCar(Car):

    def __init__(self, color, name, is_polise = True):
        Car.__init__(self, color, name, is_polise)


kia = TownCar('black', 'kia')
ferrari = SportCar ('red', 'ferrari')
gaz = WorkCar('orange', 'gaz')
uaz = PoliceCar('white', 'uaz')

kia.turn()
ferrari.turn()
gaz.turn()
uaz.turn()

