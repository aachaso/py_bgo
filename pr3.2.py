
questions_list = ['имя: ', 'фамилия: ', 'год рождения: ', 'город проживания: ', 'email: ', 'телефон: ']
user_answer = []
for el in questions_list:
    user_answer.append(input(f'Введите {el}'))

def info_about_user(questoin, answer):
    print(questoin[0] + answer[0], questoin[1] + answer[1],
          questoin[2] + answer[2], questoin[3] + answer[3],
          questoin[4] + answer[4])



info_about_user(questoin = questions_list, answer = user_answer)