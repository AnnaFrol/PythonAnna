number = int(input('Введите четырехзначное число: '))
thousands = number // 1000
num1 = number - thousands * 1000
hundrets = num1 // 100
num2 = num1 -hundrets * 100
dozens = num2 // 10
units = num2 - dozens * 10
print(thousands ,hundrets ,dozens ,units)
