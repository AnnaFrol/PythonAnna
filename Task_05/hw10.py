start_point = 0
end_point = 100
true = 1
while true:
    number = int((start_point + end_point) / 2)
    print('Твой номер меньше/больше чем число', number,'? 1 — равно, 2 — больше, 3 — меньше. ')
    check = int(input())
    if check == 2:
        start_point = number
    elif check == 3:
        end_point = number
    elif check == 1:
        print('Твой номер ', number)
        break