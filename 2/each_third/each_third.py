if __name__ == '__main__':
    print('Task 11. Each third')
s  = input("Enter a sequence of characters separated by commas: ")
characters = [x.strip() for x in s.split(',')]
third_elements = characters[::3]
print(third_elements)
