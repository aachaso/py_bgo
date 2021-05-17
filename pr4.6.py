from itertools import count, cycle

my_list = []

def my_func_count(start_number, finish_number):
    for el in count(start_number):
        if el > finish_number:
            print(', '.join(my_list))
            break
        else:
            my_list.append(str(el))

my_func_count (start_number = int(input("Введите число для старта: ")), finish_number = int(input("Введите число финиша: ")))

def my_func_cycle(user_list, num_repeat):
        i = 0
        iter = cycle(user_list)
        while i < num_repeat:
            print(next(iter))
            i += 1

my_func_cycle (user_list = my_list, num_repeat = int(input("Введите количество повторов: ")))