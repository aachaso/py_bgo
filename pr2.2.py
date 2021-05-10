user_len = int(input('Enter length your list - '))
user_list = []
i = 0
el = 0

while i < user_len:
    user_list.append(input('Enter value your list - '))
    i += 1

for v in range(int(len(user_list) / 2)):
    user_list[el], user_list[el + 1] = user_list[el + 1], user_list[el]
    el += 2

print(user_list)