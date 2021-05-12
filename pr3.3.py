def my_func(num_one, num_two, num_three):
    user_list = [num_one, num_two, num_three]
    user_list.sort()
    print(user_list[2] + user_list[1])


my_func(int(input('Введите первое число: ')), int(input('Введите втоорое число: ')), int(input('Введите третье число: ')))
