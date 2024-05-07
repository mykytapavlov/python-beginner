x = input("Enter X: ")
y = input('Enter Y: ')

if int(x) > int(y):
    print(x, 'is greater than', y)
elif int(x) < int(y):
    print(x, 'is less than', y)
else:
    print(x, 'equals', y)
