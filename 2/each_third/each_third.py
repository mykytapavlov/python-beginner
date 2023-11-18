if __name__ == '__main__':
    print('Task 11. Each third')
    user_input = input('Enter sequence: ')
    strings_sequence = user_input.split(',')
    result = [item.strip() for index, item in enumerate(strings_sequence) if (index + 1) % 3 == 0]
    print(result)