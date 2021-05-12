def my_func(x, y):
    #x ** y
    res = 1
    for i in range (1,abs(y)+1):
        res *= 1/x
    print(round(res, 3))

my_func(int(input('Введите положительное число: ')), int(input('Введите целое отрицательное число: ')))