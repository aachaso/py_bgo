def my_sum ():
    ex = False
    sum_num = 0
    while ex == False:
        number = input('Введите числа через пробел. Для выхода введите Q: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res += int(number[el])
        sum_num += res
        print(f'Сумма чисел равна: {sum_num}')

my_sum()