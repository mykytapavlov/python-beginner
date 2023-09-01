if __name__ == '__main__':
    print('Task 12. Equal parts')
    numbers = [value for value in input().split(',')]
    split_index = len(numbers) // 2
    print(f'{numbers[:split_index]} {numbers[split_index:]}')
