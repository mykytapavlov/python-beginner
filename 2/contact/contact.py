if __name__ == '__main__':
    print('Task 14. Contact.')
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    address = input('Enter your address: ')
    phone = ''.join([str(int(number)) for number in input('Enter your phone: ')])

    contact = dict(name=name, age=age, address=address, phone=phone)
    print(f'Contact created: {contact}')
