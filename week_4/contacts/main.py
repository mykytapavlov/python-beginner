from week_4.contacts.contact_list import ContactList
from week_4.contacts.contact import Contact
if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = ContactList()
    contact = Contact()
    contact.name, contact.email, contact.age = "Andriy", "qwerty@example.com", 35
    contact_list.append(contact)

    contact.email = "qwerty"
    #contact_list.append(Contact(name='Mary', email='jacke@xample.com', age=32))
    contact_list.print_content()
    #contact.name, contact.email, contact.age = "Andriy", "qwerty@example.com", -1
    print(contact.name, contact._name)
    print(contact.email + contact.name)