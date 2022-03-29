order = int(input('Введите кол-во заказов: '))
main_dict = {}
for i in range(order):
    surname, pizza, num = input(f' {i + 1} заказ: ').split()

