num = int(input('Введите число: '))
i = 1
while num // 10 != 0:
    i = i +1
    num = num // 10
print (i)