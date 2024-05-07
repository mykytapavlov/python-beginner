word = input('Please provide a word: ')
letter = input('Please provide a letter: ')

if letter in word:
    print(word, 'contains', letter)
else:
    print(word, 'doesn\'t contain', letter)
