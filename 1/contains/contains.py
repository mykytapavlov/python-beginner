if __name__ == '__main__':

    a = input('Enter some word: ')
    b = input('Enter some letter: ')
#    c = a.__contains__(b)
    if b in a:
        print(a, 'contains', b)
    else:
        print(a, 'does not contain', b)

# do not use __contains...  use b in a