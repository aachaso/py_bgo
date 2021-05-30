class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []
while True:
    try:
        user_num = input('Для выхода введите q. Для запуска введите число в список: ')
        if user_num == 'q' or user_num =='Q' or user_num == 'й':
            print(user_list)
            break
        elif not user_num.isdigit():
            raise OwnError('Нужно ввести число! Повторите. Для выхода введите q')
        user_list.append(int(user_num))
    except OwnError as err:
        print(err)

