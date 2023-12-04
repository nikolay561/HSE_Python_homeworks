word = input('Введите слово: ')

if len(word) % 2 == 0:
    list[:0] = word
    char_1 = round(len(word)/2) - 1
    char_2 = round(len(word)/2) + 1
    print(word[char_1:char_2])
else:
    list[:0] = word
    char = round(len(word)/2) - 1
    print(word[char])