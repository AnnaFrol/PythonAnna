print("Введите три разных числа: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2:
    max_num = num1
else:
    max_num = num2
if num3 > max_num:
    max_num = num3
print("Максимальное из 3-ёх чисел: ", max_num)