if __name__ == '__main__':
    print('Task 15. Unique.')

s = input("Enter a sequence of numbers separated by commas: ")
numbers = [int(x.strip()) for x in s.split(',')]
unique_numbers = sorted(set(numbers))
print("Unique:", ", ".join(map(str, unique_numbers)))
print("Occurrences:")
for num in unique_numbers:
    print(f"{num}: {numbers.count(num)}")
