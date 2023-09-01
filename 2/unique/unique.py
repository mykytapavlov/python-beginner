if __name__ == '__main__':
    print('Task 15. Unique.')
    unique_sequence = sorted(set(int(value) for value in input().split(',')))
    print(f'Unique: {", ".join(str(number) for number in unique_sequence)}')
