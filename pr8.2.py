class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    user_divider = int(input("Введите положительное число: "))
    user_denominator = int(input("Введите положительное число: "))
    if user_denominator == 0:
        raise OwnError("error: Деление на 0")
except OwnError as err:
    print(err)
except ValueError:
    print("Вы ввели символ")
else:
    print(f"Результат деления: {user_divider/user_denominator}")

