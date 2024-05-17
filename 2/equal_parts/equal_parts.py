some_string = input('Enter any sentence: ').split()
list_length = int(len(some_string)/2)
print(list_length)

print(some_string[:list_length])
print(some_string[list_length:])

