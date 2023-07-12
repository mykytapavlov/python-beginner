if __name__ == '__main__':
    print('Task 15. Unique.')
my_txt = input('Enter the sequence of numbers with random comma: ')
x = my_txt.replace(',', ' ')
y = set(x.split())
z = list(y)
a = [int(item) for item in z]
b = sorted(a)
c = [str(item) for item in b]
print(', '.join(c))
for item in my_txt:
    print(item, my_txt.count(item))

#ready