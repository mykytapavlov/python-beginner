if __name__ == '__main__':
    print('Task 14. Contact.')
    name = input('Enter your name: ')
    name = name.capitalize()
    age = input('Enter your age: ')
    age = int(age)
    address = input('Enter your address: ')
    address = address.capitalize()
    phone = input('Enter your phone: ')
    contact_info = {'name': name, 'age':age, 'address':address, 'phone':phone}
    print('Contact created: ', contact_info)