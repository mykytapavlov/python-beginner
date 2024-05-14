if __name__ == '__main__':
    print('Task 10. Sort numbers')
    s = input("Input your list of numbers separated by ', ': ")
    numbers = [int(a) for a in s.split(', ')]
    numbers.sort()
    print("Sorted list:")
    print(numbers)
