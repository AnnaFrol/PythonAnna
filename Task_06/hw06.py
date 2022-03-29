N = int(input('Введите количество учеников в классе: '))
num3 = 0
num4 = 0
num5 = 0
for i in range(1, N+1):
    mark = int(input('Введите оценку: '))
    if mark == 3:
        num3 = num3 + 1
    elif mark == 4:
        num4 = num4 + 1
    elif mark == 5:
        num5 = num5 + 1
if num3 > num4 and num3 > num5:
    print('Троечников сегодня', num3)
elif num4 > num5 and num4 > num3:
    print('Хорошистов сегодня', num4)
else:
    print('Отличников сегодня', num5)