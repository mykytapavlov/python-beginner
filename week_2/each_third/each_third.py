if __name__ == '__main__':
    print('Task 11. Each third')
txt = input('Enter sequence of values with random spacing between each (no comma needed): ')
x = txt.split()
print('x: ', x, id(x))
y = x[::3]
print(y)
#you can use select all => add step
#list
#for now leave as it is