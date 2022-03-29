sum = 0
for number in range(12):
    number = int(input('Введите свою зарплату за месяц: '))
    sum = sum + number
average = sum/12
print('Средняя зарплата за год: ', average)