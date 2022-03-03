chair1 = int(input('Стоимость 1 стула: '))
chair2 = int(input('Стоимость 2 стула: '))
chair3 = int(input('Стоимость 3 стула: '))
sum = chair1 + chair2 + chair3
if sum >= 10000 :
    check1 = sum - (sum / 10)
    print('Ваша сумма: ',check1)
else:
    print('Ваша сумма: ',sum)