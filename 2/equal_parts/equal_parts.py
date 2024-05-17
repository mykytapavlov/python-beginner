if __name__ == '__main__':
    print('Task 12. Equal parts')
   
s = input("Enter a sequence of characters separated by commas: ")
characters = [x.strip() for x in s.split(',')]
midpoint = (len(characters) + 1) // 2
first_part = characters[:midpoint]
second_part = characters[midpoint:]
print(first_part, second_part)
