square = int(input('Введите площадь квартиры: '))
price = int(input('Введите стоимость: '))
if square >= 100 and price <= 10 or square >= 80 and price <= 7:
    print('Эта квартира подходит!')
else:
    print('Будем искать еще(')