x = float(input('Введите сумму вклада: '))
p = int(input('Введите проценты: '))
y = float(input('Введите конечное значение: '))
years = 0
while x <= y:
    years = years + 1
    x = x * (1 + p / 100)
    x = round(x)
print('Вам понадобится', years, 'лет')
