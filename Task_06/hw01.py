numbers = [11, 21, 22, 7896, 890]
for number in numbers:
    if number // 2 == 0 and number // 3 != 0:
        print('Число подходит')
    else:
        print('Число не подходит')