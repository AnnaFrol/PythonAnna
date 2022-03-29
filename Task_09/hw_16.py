
first_list = input('это первый список. введи числа через пробел. \n> ').split()
second_list = input('это второй список. введи числа через пробел. \n> ').split()
first_list.extend(second_list)
first_list = list(set(first_list))
print(f'Новый первый список с уникальными элементами: { first_list } ')