month = int(input('Enter month as its ordinal in the year - '))

season = ['winter', 'spring', 'summer', 'fall']

if month == 1 or month == 12 or month == 2:
    print(season[0])
elif month == 3 or month == 4 or month == 5:
    print(season[1])
elif month == 6 or month == 7 or month == 8:
    print(season[2])
elif month == 9 or month == 10 or month == 11:
    print(season[3])
else:
    print("Error")

month = int(input('Repeat. Enter month as its ordinal in the year - '))
season_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'fall'}

if month == 1 or month == 2 or month == 12:
    print(season_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(season_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(3))
elif month == 10 or month == 11 or month == 9:
    print(season_dict.get(4))
else:
    print('End')