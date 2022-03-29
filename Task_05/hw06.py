print('Введите последовательность: ')
n = 0
i = 1
plus = 0
minus = 0
while i != 0:
    i = int(input(''))
    if i > 0:
        plus = plus + 1
    else:
        minus = minus + 1
minus = minus - 1
print('Кол-во положительных чисел: ', plus)
print('Кол-во отрицательных чисел: ', minus)