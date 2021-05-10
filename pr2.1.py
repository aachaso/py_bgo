a = ['a', 'b', 1, 2.3, True]
c = 0


while len(a) > 0:
    print(type(a[c]))
    a.pop(c)

print('end')