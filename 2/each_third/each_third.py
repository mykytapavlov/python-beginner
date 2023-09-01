if __name__ == '__main__':
    print('Task 11. Each third')
    numbers = [value for value in input().split(',')]
    numbers = numbers[0:len(numbers):2]
    print(numbers)
