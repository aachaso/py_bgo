user_words = input('Enter several words sep for string - ')
user_words = user_words.split()


for num, el in enumerate(user_words):
    if len(el) > 10:
        el = el[0:10]
    print(f'№{num}. {el}')