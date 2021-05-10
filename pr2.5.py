user_number = int(input("Enter number - "))
my_list = [7, 6, 5, 4, 3, 2, 1]
c = my_list.count(user_number)

for element in my_list:
    if c > 0:
        i = my_list.index(user_number)
        my_list.insert(i+c, user_number)
        break
    else:
        if user_number > element:
            j = my_list.index(element)
            my_list.insert(j, user_number)
            break
        elif user_number < my_list[len(my_list) - 1]:
            my_list.append(user_number)
print(my_list)