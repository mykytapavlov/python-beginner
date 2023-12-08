from contact import create_contact
from contact_list import ContactList

if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = ContactList()

    while True:
        try:
            name = input('name: ')
            email = input('email: ')
            age = input('age: ')
            new_contact = create_contact(name, email, age)
        except ValueError as e:
            print(e)
            continue

        print('-' * 10)
        print(new_contact)
        print('-' * 10)

        contact_list.append(new_contact)
        proceed = input('add another one? (y/n): ')

        if proceed.lower() != 'y':
            break

    print('Contact List:')
    for contact in contact_list:
        print(contact)
