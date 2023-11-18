if __name__ == '__main__':
    print('Task 12. Equal parts')
    user_input = input('Enter sequence: ')
    strings_sequence = user_input.split(',')
    sequence_middle = int(len(strings_sequence)/2)
    first_part = strings_sequence[:sequence_middle]
    second_part = strings_sequence[sequence_middle:]
    print(first_part, second_part)