if __name__ == '__main__':
    print('Task 9. Contains?')

word = input("enter word: ")
letter = input("enter letter: ")

if letter in word:
    print("letter",letter,"is in the word",word)
else:
    print("letter",letter,"is not in the word",word)
