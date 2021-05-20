my_list = ['Hello\n', '30.5\n', 'line 3\n']

with open("test_2.txt", 'w+') as my_file:
    my_file.writelines(my_list)

with open("test_2.txt") as my_file:
    num_lines = 0
    num_words = 0
    for line in my_file:
        num_lines += line.count("\n")
        num_words = len(line)-1
        print(f"Количество символов в строке {num_lines} - {num_words}")
    print(f"Всего строк в файле {num_lines}")