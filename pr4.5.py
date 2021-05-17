from functools import reduce

def func_times(prev, elem):
    return prev * elem

print(reduce(func_times, [el for el in range(100, 1001) if el % 2 == 0]))