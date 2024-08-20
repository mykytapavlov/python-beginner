word = 'collaboration'
# if "a" in word:
#     print(word)
# else:
#     print(word[::-1])

letter = input('Enter a letter:').lower()
if letter not in word:
    print('Incorrect letter')
else:
    print(word)


