class Contact:
    def __init__(self):
        self._name = None
        self._email = None
        self._age = None


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        if len(self.name) > 50:
            raise ValueError('Name is too large!')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
        if '@' not in self.email or '.' not in self.email:
            raise ValueError('Invalid email!')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
        try:
            age = int(self.age)
            if age <= 0:
                raise ValueError
        except ValueError:
            raise ValueError('Invalid age!')

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"

def create_contact(name, email, age):
    new_contact = Contact()
    new_contact.name = name
    new_contact.email = email
    new_contact.age = age
    return new_contact
