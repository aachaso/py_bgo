user_integer = abs(int(input('Enter the number - ')))
max_numerical = user_integer % 10

while user_integer > 0:
    if user_integer % 10 > max_numerical:
        max_numerical = user_integer % 10
    user_integer = user_integer // 10

print(f'The largest numerical in your number - {max_numerical}')
