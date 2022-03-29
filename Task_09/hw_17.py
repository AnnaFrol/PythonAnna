h = []
s = []
count = 0
size_num = int(input('Кол-во коньков: '))
for i in range(1, size_num + 1):
    s.append(int(input(f'Размер  {i} пары: ')))
hum_num = int(input('Кол-во людей: '))
for i in range(1, hum_num + 1):
     h.append(int(input(f'Размер ноги {i} человека:  ')))
for num in h:
    for j in range(len(s)):
        if s[j] == num:
            count = count + 1
            break
print('Наибольшее кол-во людей, которые могут взять ролики: ', count)