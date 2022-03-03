mileage = int(input('Введите пробег: '))
date = int(input('Введите сегодняшнее число: '))
a = mileage // 100
b = mileage - a
c = b // 10
d = b % 10
sum = a + c + d
if sum > date :
    print('Сброс\n','Пробег: 0')
else:
    print('Сегодня не сломался\n','Пробег: ',mileage)