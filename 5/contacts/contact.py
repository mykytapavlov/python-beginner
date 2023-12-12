class Contact:
    def __init__(self):
        self._age = None
        self._name = None
        self._email = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age < 90:
            self._age = age
        else:
            raise ValueError(f'Incorrect age. Wrong type for age or age is more that 90')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) <= 50:
            self._name = name.capitalize()
        else:
            raise ValueError('Name is too large!')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' in email and '.' in email:
            self._email = email
        else:
            raise ValueError('Invalid email!')

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}, Email: {self._email}"


if __name__ == '__main__':
    mike = Contact()
    mike.age = 89
    mike.name = 'Mike'
    mike.email = 'mike@test.com'
    print(f'hello: {mike.name}, {mike.age} year(s), {mike.email}')
