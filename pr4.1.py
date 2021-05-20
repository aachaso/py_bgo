user_list = []

while True:
    line = input("Введите любое значение: ")
    if line == '':
        exit()
    else:
        new_line = line + '\n'
        user_list.append(new_line)

    with open("test_1.txt", "w") as user_file:
        user_file.writelines(user_list)