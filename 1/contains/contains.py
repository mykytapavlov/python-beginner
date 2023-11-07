if __name__ == '__main__':
    print('Task 9. Contains?')
    word = input('Type any word: ')
    letter = input('Type any letter: ')

    if letter in word:
        print('The word contains the entered letter')
    else:
        print('The letter was not found in the entered word')