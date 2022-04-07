X = int(input('Введите количество мальчиков: '))
Y = int(input('Введите количество девочек: '))
answer = ''
if (X > 2 * Y) or (Y > 2 * X):
    print('Нет решения.')
elif X >= Y:
    k = X - Y
    for i in range(k):
        answer += 'BGB'
    for a in range(Y - k):
        answer += 'BG'
else:
    k = X - Y
    for b in range(k):
        answer += 'GBG'
    for c in range(X - k):
        answer += 'GB'
print(answer)


