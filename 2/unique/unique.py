if __name__ == '__main__':
    print('Task 15. Unique.')
    s = input("Enter your sequence of numbers: ")
    s.replace(" ", "")
    numbers = [int(a) for a in s.split(',')]
    unique = list(set(numbers))
    unique.sort()
    print(f"Unique numbers from your sequence: {unique}")
    for i in range(len(unique)):
        print(f"Number {unique[i]} occurs in your sequence {numbers.count(unique[i])} times")
