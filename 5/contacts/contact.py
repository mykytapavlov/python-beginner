class Contact:
    def __init__(self, name=None, email=None, age=None):
        self.name = name
        self.email = email
        self.age = age

    def validate_name(self):
        if len(self.name) > 50:
            raise ValueError('Name is too large!')

    def validate_email(self):
        if '@' not in self.email or '.' not in self.email:
            raise ValueError('Invalid email!')

    def validate_age(self):
        try:
            age = int(self.age)
            if age <= 0:
                raise ValueError
        except ValueError:
            raise ValueError('Invalid age!')

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"

def create_contact(name, email, age):
    new_contact = Contact(name, email, age)
    new_contact.validate_name()
    new_contact.validate_email()
    new_contact.validate_age()
    return new_contact
