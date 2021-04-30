first_day_km = int(input('Enter your running result in 1 day,km - '))
target = int(input('Enter your goal,km - '))
day = 1
while target - first_day_km > 0:
    first_day_km = first_day_km + (first_day_km * 0.1)
    day += 1
print(f'If you increase the distance every day by 10%, then you will reach the goal in {day} days.')
