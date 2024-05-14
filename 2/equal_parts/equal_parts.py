if __name__ == '__main__':
    print('Task 12. Equal parts')
    s = input("Input your sequence of characters separated by ', ': ")
    sequence = s.split(', ')
    print("Your sequence split it on 2 (mostly) equal parts:")
    print(sequence[:len(sequence)//2], sequence[len(sequence)//2:])
