if __name__ == '__main__':
    print('Task 11. Each third')
    s = input("Input your sequence of characters separated by ', ': ")
    sequence = s.split(', ')
    print("List of each third element:")
    print(sequence[2::3])
