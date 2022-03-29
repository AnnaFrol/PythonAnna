for i in range(30, 36, 1):
    number = int(input(f'Людей в {i} -м секторе: '))
    if number > 10:
        print('Нарушение! Слишком много людей в секторе!')
    else:
        print('Всё спокойно.')
