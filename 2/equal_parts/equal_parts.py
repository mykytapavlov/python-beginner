if __name__ == '__main__':
    print('Task 12. Equal parts')
a=input("Enter a sequence of characters:")
print(a)
print (a.replace(" ", ""))
a= a.replace(" ", "")
splited_input_value=a.split(",")
print (splited_input_value)
len(splited_input_value)
print(len(splited_input_value))
lenght= len(splited_input_value) // 2
first_half = splited_input_value[:lenght]
second_half = splited_input_value[lenght:]
print(first_half, second_half)