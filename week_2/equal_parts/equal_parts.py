if __name__ == '__main__':
    print('Task 12. Equal parts')
txt = input('Enter sequence of 8 values with random spacing between each (no comma needed): ')
x = txt.split()
print('x: ', x, id(x))
y = x[0:4]
d = x[4:]
print(y, d)
#list
#ready