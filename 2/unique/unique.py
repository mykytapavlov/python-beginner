if __name__ == '__main__':
    print('Task 15. Unique.')
    not_unique = [1, 2, 5, 4, 1, 2, 2, 3, 5, 8, 6, 7, 3, 8, 9, 6, 7, 4, 9]
    unique = list(set(not_unique))
    unique.sort()
    print(unique)