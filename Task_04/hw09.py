salary = float(input('Введите вашу зарплату: '))
if salary < 10000:
    print('Без налогов')
elif 50000 > salary >= 10000:
    print('Налог: ', 10000 * 0.13 + (salary - 10000) * 0.20)
else:
    print('Налог: ', 10000 * 0.13 + 40000 * 0.20 + 0.3 * (salary - 50000))