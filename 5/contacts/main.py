from contact import Contact
from contact_list import ContactList

if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = ContactList()

    while True:
        try:
            name = input('name: ')
            email = input('email: ')
            age = input('age: ')

            contact = Contact(name=name, email=email, age=age)
        except ValueError as e:
            print(e)
            continue

        contact_list.append(contact)

        print('-' * 10)
        print(contact)
        print('-' * 10)

        proceed = input('add another one? (y/n): ')

        if proceed != 'y':
            break

    print("\nContact List:")
    print(contact_list)
