str1 = input('Первая строка: ')
str2 = input('Вторая строка: ')
if str1 == str2:
    print('Строки идентичны')
elif len(str1) != len(str2):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    k = 1
    mozhno = False
    for i in range(len(str2) - 1):
        str2 = str2[-1] + str2[:-1]
        if str2 == str1:
            mozhno = True
            print('Первая строка получается из второй со сдвигом ',k)
            break
        else:
            k += 1
    if not mozhno:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')