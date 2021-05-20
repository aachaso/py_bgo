lesson_dict = {}

with open('test_6.txt', 'r', encoding='utf-8') as file_less:
    for line in file_less:
        study_list = line.split()
        name_lesson = study_list[0].strip(':')
        sum_les = 0
        for elem in study_list:
            num = '0'
            for i in elem:
                if i.isdigit():
                    num += i
            sum_les += int(num)
        lesson_dict[name_lesson] = sum_les
print(lesson_dict)
