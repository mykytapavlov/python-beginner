if __name__ == '__main__':

    a = 'convention'
    b = 't'
    c = a.__contains__(b)
    if c is True:
        print(a, 'contains', b)
    else:
        print(a, 'does not contain', b)
