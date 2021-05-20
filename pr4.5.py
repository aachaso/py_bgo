def sum_num():
    try:
        with open('test_5.txt', 'w+') as file_num:
            line = input('Введите числа через пробел: ')
            file_num.writelines(line)
            my_numb = line.split()
            total_sum = sum(map(int, my_numb))
            print(f'Сумма чисел {line} = {total_sum}')
    except IOError:
        print('Произошла ошибка ввода-вывода!')
    except ValueError:
        print('Неправильное значение числа!')
sum_num()