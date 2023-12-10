from contact import Contact


# ContactList is a custom class which stores only an instances of class Contact.
# It does not support methods of built-in `list` data type
# (since it's not inherited from it, so the only thing related to the lists is actually a class name)
# Python does not care about class names, it's for people more.
# But Python cares about protocols.
# If you want to say that something is a list to Python, that something should have specific methods implemented.
# If you implement special methods required for Iterator Protocol, for example,
# you will be able to do for loops with your custom list.


class ContactList:
    def __init__(self):
        self.storage = []
        self.index = 0

    def append(self, user):
        self.storage.append(user)
        self.index += 1

    def __iter__(self):
        self._current_index = 0
        return self

    def __next__(self):
        if self._current_index < len(self.storage):
            current_user = self.storage[self._current_index]
            self._current_index += 1
            return current_user
        else:
            raise StopIteration

    def __str__(self):
        all_users_list = []
        for user in self.storage:
            all_users_list.append(f"Name: {user.name}, Age: {user.age}, Email: {user.email}")
        return f"\n" .join(all_users_list) + f'\ntotal amount= {len(self.storage)}'

    # Remember I told, that if you want to print your custom class nicely,
    # you need to defined __str__ method and tell python what to print exactly.

    # Read this section: https://realpython.com/python-iterators-iterables/#what-is-the-python-iterator-protocol


if __name__ == '__main__':
    contact_list = ContactList()
    mike = Contact(name='Mike', email='mike@example.com', age=30)
    sem = Contact(name='Sem', email='sem@example.com', age=45)
    # should append only instances of Contact class
    contact_list.append(mike)
    contact_list.append(sem)

    # should print list of contacts nicely as well as total amount
    print(contact_list)

    print("======================")
    # should print each contact nicely
    for contact in contact_list:
        print(contact)
