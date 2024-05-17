if __name__ == '__main__':
    print('Task 10. Sort numbers')

s = input("Enter a sequence of numbers separated by commas: ")
numbers = [int(x.strip()) for x in s.split(',')]
sorted_numbers = sorted(numbers)
print("Output:", sorted_numbers)
