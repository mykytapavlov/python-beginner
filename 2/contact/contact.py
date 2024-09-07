if __name__ == '__main__':

    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    address = input('Please enter your address: ')
    phone = input('Please enter your phone: ')

#    contact_data = (name, age, address, phone)
#    contact_keys = ('name', 'age', 'address', 'phone')
#    contact = dict.fromkeys(contact_keys, name)

    contact = {}
    contact['name'] = name
    contact['age'] = age
    contact['address'] = address
    contact['phone'] = phone


    print('Contact created: ', contact)
