hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))
sum = hours + credit + food
salary = (200 * hours) / ( 2** 3) + hours
if salary >= sum:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')