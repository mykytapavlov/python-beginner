if __name__ == '__main__':
    print('Task 10. Sort numbers')
a=input("Enter a sequence of numbers:")
a='3, 2, 1, 4, 5,  2'
print(a)
input_string = '3, 2, 1, 4, 5,  2'
numbers = a.split(",")
print(numbers)
a=sorted([3, 2, 1, 4, 5,  2])
print("Sorted in ascending order: ",a)