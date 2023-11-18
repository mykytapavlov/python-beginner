if __name__ == '__main__':
    print('Task 10. Sort numbers')
    user_input = input('Enter sequence: ')
    strings_sequence = user_input.split(', ')
    sequence = [int(item) for item in strings_sequence]
    sequence.sort()
    print(sequence)
