from sys import argv

script_name, working_hour, rate, bonus = argv
salary = (int(working_hour) * int(rate)) + int(bonus)
print(salary)