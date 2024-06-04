from contact import Contact


if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = []

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
