from time import sleep

class TrafficLight:
    __color = ['Красный сигнал', 'Желтый сигнал', 'Зеленый сигнал']

    def change_color(self):
        i = 0
        while i < 3:
            print(f'{self.__color[i]}')
            if i == 0:
                sleep(7)
                print('Переключение светофора')
            elif i == 1:
                sleep(2)
                print('Переключение светофора')
            elif i == 2:
                sleep(7)
            i += 1


trafic = TrafficLight()
trafic.change_color()