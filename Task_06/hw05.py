factorial_n = 1
n = int(input('Введите число: '))
for i in range(2, n + 1, 1):
    factorial_n = factorial_n * i
print('Факториал числа: ', factorial_n)
