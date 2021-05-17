
user_num = input('Введите числа через пробел - ').split()

user_list = [int(num) for num in user_num]

new_list = [el for el in user_list if el > user_list[user_list.index(el) - 1]]
print(new_list)