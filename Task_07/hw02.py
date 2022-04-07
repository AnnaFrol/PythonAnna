N = int(input('Введите количество должников: '))
sum = 0
for i in range(N//5 + 1):
    print('Должник с номером ', i*5)
    print('Сколько должны? ')
    duty = int(input())
    sum += duty
print('Общая сумма долга: ', sum)