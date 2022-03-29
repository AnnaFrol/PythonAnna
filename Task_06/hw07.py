a = int(input('Введите левый предел: '))
b = int(input('Введите правий предел: '))
sum = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum = sum + i
        count = count + 1
average = sum / count
print('Среднее арифметическое чисел кратных 3: ', average)