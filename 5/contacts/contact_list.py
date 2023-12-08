from contact import Contact
class ContactList:
    def __init__(self):
        self.storage = []

    def append(self, contact):
        if not isinstance(contact, Contact):
            raise ValueError("Not in Contact class")
        self.storage.append(contact)

    def __str__(self):
        return '\n'.join(map(str, self.storage))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.storage):
            result = self.storage[self.index]
            self.index += 1
            return result
        raise StopIteration
