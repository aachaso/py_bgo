user_num = input('Введите числа через пробел - ').split()

user_list = [int(num) for num in user_num]

new = [el for el in user_list if user_list.count(el) == 1]
print(new) 