educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы: '))
mes = expenses - educational_grant
for i in range(9):
    expenses *= 1.03
    difference = expenses - educational_grant
    mes += difference
print('У родителей необходимо попросить ', mes)
