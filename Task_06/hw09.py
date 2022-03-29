numbers = input('Введите 10 чисел: ').split()
numbers = list(map(int, numbers))
n = 0
for i in range(len(numbers) - 1):
    if numbers[i+1] < numbers[i]:
        n += 1
print(numbers)
if n == 0:
    print('Числа упорядочены по возрастанию')
else:
    print('Числа не упорядочены по возрастанию')