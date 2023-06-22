if __name__ == '__main__':
    print('Task 10. Sort numbers')
txt = input('Enter several numbers with random spacing between each (no comma needed): ')
x = txt.split()
print('x: ', x, id(x))
y = [int(item) for item in x]
y.sort()
print('y: ', y, id(y))
# list
# ready