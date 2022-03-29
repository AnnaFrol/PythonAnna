import random
number = random.randint(0, 100)
users_number = -1
tries = 1
while users_number != number:
    users_number = int(input('Введи свое число: '))
    if users_number < number:
        print('Твое число меньше моего. Попробуй еще раз.')
    elif users_number > number:
        print('Твое число больше моего. Попробуй еще раз.')
    else:
        print('Вы угадали! ')
        break
    tries = tries + 1
print('Число попыток: ', tries)