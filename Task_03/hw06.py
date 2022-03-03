Kostya = int(input('Кубик Кости: '))
owner = int(input('Кубик владельца: '))
if Kostya < owner:
    sum = Kostya + owner
    print('Сумма: ',sum, '\n','Владелец платит\n','Игра окончена')
else:
    print('Разность: ',Kostya - owner,'\n', 'Костя платит\n','Игра окончена')

