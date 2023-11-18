if __name__ == '__main__':
    print('Task 15. Unique.')

    user_input = input('Enter sequence: ')
    strings_sequence = user_input.split(',')
    sequence = [int(item.strip()) for item in strings_sequence]
    print(f'Result: {tuple(set(sequence))}')

    occurence_number = input('Enter number to check amount of occurences: ')
    print(sequence.count(int(occurence_number)))