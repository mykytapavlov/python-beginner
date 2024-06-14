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

    # Remember I told, that if you want to print your custom class nicely,
    # you need to defined __str__ method and tell python what to print exactly.

    # Read this section: https://realpython.com/python-iterators-iterables/#what-is-the-python-iterator-protocol

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.storage):
            item = self.storage[self.index]
            self.index += 1
            return item
        else:
            self.index = 0
            raise StopIteration

    def __str__(self):
        output = '\n' + 10 * '*' + '\nContact List:\n'
        for item in self:
            output = output + str(item) + '\n'
        output = output + 'Total amount of contacts: ' + str(len(self.storage)) + '\nEnd of Contact List\n' + 10 * '*' + '\n'
        return output

    def append(self, new_contact):
        if isinstance(new_contact, Contact):
            self.storage.append(new_contact)
        else:
            raise ValueError('Invalid Contact Format')
