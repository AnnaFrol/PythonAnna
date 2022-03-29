number = int(input('Введите количество пар слов: '))
main_dict = {}
for i in range(number):
    word_fst, snd_word = input(f' {i + 1} пара: ').split()
    main_dict[word_fst] = snd_word
word = input('Введите слово: ')
print('Синоним:', main_dict.get(word) or ''.join([word_fst \
for word_fst, snd_word in main_dict.items() if snd_word == word]) or 'Такого слова в словаре нет')