a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите число для сравнения: '))
sum = 0
count = 0
for i in range(a, b +1):
    if i % c ==0:
        count += 1
        sum += i
if count == 0:
    print('Расчет невозможен.')
else:
    print('Среднее арифметическое = ', sum / count)