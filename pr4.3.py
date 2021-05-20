employee_dict = {'Ivanov': 50000, 'Petrov': 15000, 'Sidorova': 21000, 'Popova': 16000, 'Orlov': 30000}

try:
    employee_file = open("test_3.txt", 'w')
    for last_name, salary in employee_dict.items():
        employee_file.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    employee_file.close()

total_income = 0
count_emploee = 0
persons = []

with open("test_3.txt", "r") as emp_file:
    for line in emp_file:
        print(line, end="")
        search_line = line.split(':')
        if int(search_line[1]) <= 20000:
            persons.append(search_line[0])
        total_income += int(search_line[1])
        count_emploee += 1
result = total_income / count_emploee
print(f"Сотрудники, с зп менее 20 тыс: {persons}")
print(f"Средний уровень зп: {result}")