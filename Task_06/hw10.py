N = int(input('Введите количество карточек: '))
initial_cards = []
cards = input('Введите карточки от 1 до N-1').split()
for i in range(1, N + 1):
    initial_cards.append(str(i))
result = list(set(initial_cards) ^ set(cards))
print(result)