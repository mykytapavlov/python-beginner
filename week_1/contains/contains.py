word = input('Enter word: ')
letter = input('Enter letter: ')

print(letter.casefold() in word.casefold())
