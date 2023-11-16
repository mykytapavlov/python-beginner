x = input('Enter a number: ')
y = input('Enter a number: ')
z = input('Enter a number: ')
try:
    float(x), float(y), float(z)
except ValueError:
    print('incorrect number, please rerun script and enter correct numbers')
else:
    print(f'Coordinate ({x}, {y}, {z})')
