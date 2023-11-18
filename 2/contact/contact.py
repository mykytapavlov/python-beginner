if __name__ == '__main__':
    print('Task 14. Contact.')
    name = input('Enter name: ')
    age = int(input('Enter your age: '))
    address = input('Enter address: ')
    phone = input('Enter phone: ')
    contact_hash = {'name': name, 'age': age, 'address': address, 'phone': phone}
    print(f'Contact created: {contact_hash}')