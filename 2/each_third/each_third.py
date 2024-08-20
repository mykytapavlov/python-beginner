if __name__ == '__main__':
    print('Task 11. Each third')
a=input("Enter a sequence of characters:")
print(a)
print (a.replace(" ", ""))
a= a.replace(" ", "")
splited_input_value=a.split(",")
print (splited_input_value)
print(splited_input_value[::3])