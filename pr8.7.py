class ComplexNumber:
    def __init__(self, num_one, num_two, *args):
        self.num_one = num_one
        self.num_two = num_two
        self.total = 'num_one + num_two * i'

    def __add__(self, other):
        print(f'Сумма num_one и num_two = ')
        return f'{self.num_one + other.num_one} + {self.num_two + other.num_two} * i'

    def __mul__(self, other):
        print(f'Произведение num_one и num_two = ')
        return f'{self.num_one * other.num_one - (self.num_two * other.num_two)} + {self.num_two * other.num_one} * i'

    def __str__(self):
        return f'{self.num_one} + {self.num_two} * i'


user_num_one = ComplexNumber(1, -2)
user_num_two = ComplexNumber(3, 4)
print(user_num_one)
print(user_num_one + user_num_two)
print(user_num_one * user_num_two)