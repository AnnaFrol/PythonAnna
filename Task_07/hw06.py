l1 = int(input('Введите размер стороны листа: '))
l2 = l1
convert = 12
count = 0
while convert < l1 or convert < l2:
    if convert < l1:
        count += 1
        l1 = l1 / 2
        if convert < l2:
            count += 1
            l2 = l2 / 2
print('Складывать ', count, 'раз')