number = int(input('Вставьте шестизначный номер:' ))
units = number - number//10 * 10
tens = number//10 % 10
hundreds = number//100 % 10
thousands = number//1000 % 10
ten_thousands = number//10000 % 10
hund_thousands = number//100000
if thousands + ten_thousands + hund_thousands == units + tens + hundreds:
    print('У вас счастливый билет!')
else:
    print('У вас несчастливый билет.')