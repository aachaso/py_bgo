from math import factorial


def generator(number):
    c = 0
    for el in range(1, number + 1):
        if c > number:
            break
        else:
            yield factorial(el)
            c += 1


user_list = generator(int(input('Введите количество факториалов - ')))

for i in user_list:
    print(f'Факториал {i}')
