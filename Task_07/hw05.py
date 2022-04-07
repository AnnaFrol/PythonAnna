a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
c = int(input('Введите шаг: '))
for x in range(b + 1, a, -c):
    y = x**3 + 2*x**2 - 4*x + 1
    print(y)