if __name__ == '__main__':
    print('Task 15. Unique.')
    numbers = input('Enter list of numbers: ')
    numbers = sorted(list(map(int, set(numbers.replace(' ', '').split(',')))))
    print(numbers)