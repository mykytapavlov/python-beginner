if __name__ == '__main__':
    print('Task 12. Equal parts')

a = list(input("Type here text that will be devided : "))
b = len(a)
c = int(b/2)
print(a[:c])
print(a[c:])
