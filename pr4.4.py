tranclate_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []

with open('test_4_in.txt', 'r') as file_in:
    for i in file_in:
        i = i.split(' ')
        new_file.append(tranclate_num[i[0]] + '  ' + i[2])
    print(new_file)

with open('test_4_out.txt', 'w', encoding='utf-8') as file_out:
    file_out.writelines(new_file)
