def func_dev(num1, num2):
    try:
        print(
            'Результат деления числа 1 на число 2: ', round(num1 / num2, 1),
            '\nРезультат деления числа 2 на число 1: ', round(num2 / num1, 1))
    except ZeroDivisionError:
        print('Ошибка: на ноль делить нельзя!')

func_dev(int(input('Введите число 1: ')), int(input('Введите число 2: ')))