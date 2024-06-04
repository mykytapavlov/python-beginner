from contact import Contact
from contact_list import ContactList


if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = ContactList()
    mike = Contact(name='Mike', email='mike@example.com', age=30)

    # should append only instances of Contact class
    contact_list.append(mike)

    while True:
        try:
            new_contact = Contact.create_from_input()
        except ValueError as e:
            print(e)
            continue
        print(new_contact)
        contact_list.append(new_contact)
        proceed = input('add another one? (y/n): ')
        if proceed != 'y':
            break

    # should print list of contacts nicely as well as total amount
    print(contact_list)

    # should print each contact nicely
    print('Printing each contact directly:')
    for contact in contact_list:
        print(contact)
