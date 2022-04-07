n = int(input('Введите кол-во заказов: '))
main_dict = dict()
for i in range(1, n + 1):
    print(i, 'заказ ', end = '')
    order = (input('')).split(' ')
    name = order[0]
    pizza = order[1]
    num = int(order[2])
    if name not in main_dict:
        main_dict[name] = {pizza:num}
    else:
        if pizza not in main_dict[name]:
            main_dict[name] |= {pizza: num}
        else:
            main_dict[name][pizza] += num
print(main_dict)
for fam, elem in sorted(main_dict.items()):
    for name_pizza in elem.keys():
        print(fam, ':')
        print(' ', name_pizza, ':', elem[name_pizza])



