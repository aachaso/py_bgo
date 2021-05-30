from datetime import date

class DateUser:
    def __init__(self, period):
        self.period = print('-'.join(str(x) for x in (period.day, period.month, period.year)))


    @classmethod
    def get_int_period(cls, period):
        data_list = []
        for i in ('-'.join(str(x) for x in (period.day, period.month, period.year))).split('-'):
            data_list.append(i)
        return f'{int(data_list[0])}-{int(data_list[1])}-{int(data_list[2])}, тип {type(int(data_list[0]))}'

    @staticmethod
    def date_valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 1970:
                    print(f'дата{day}-{month}-{year}')
                else:
                    print(f'Неправильно введен год {year}')
            else:
                print(f'Неправильно введен месяц {month}')
        else:
            print(f'Неправильно введен день {day}')


today_ii = DateUser(date.today())
print(today_ii.get_int_period(date.today()))
DateUser.date_valid(int(input('введите день числом ')),int(input('введите месяц числом ')),int(input('введите день год ')))

