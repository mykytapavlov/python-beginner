if __name__ == '__main__':
    #Create python program which sums 2 digits and prints result to console
    ##Should look like this:
    #Sum two digits
    #first digit: 2
    #second digit: 2.3
   # result: 4.3
   # Python Docs - look for "input" function
    print ('Sum two digits')
    num1 = input('first digit: ')
    num2 = input('second digit: ')
    sum = float(num1) + float(num2)
    print('result: {0}'.format(sum))