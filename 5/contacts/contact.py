def validate_name(name: str):
    if len(name) > 50:
        raise ValueError('Name is too large!')

    return name


def validate_email(email: str):
    if '@' not in email or '.' not in email:
        raise ValueError('Invalid email!')

    return email


def validate_age(age: int):
    try:
        if age <= 0:
            # We ask Python to raise ValueError if <= 0
            raise ValueError
    except ValueError:
        raise ValueError('Invalid age!')

    return age


class Contact:
    def __init__(self, name: str, email: str, age: int):
        self.name = validate_name(name)
        self.email = validate_email(email)
        self.age = validate_age(age)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = validate_name(name)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = validate_email(email)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = validate_age(age)

    def __str__(self):
        return f"{{'name': {self.name},'email': {self.email},'age': {self.age}}}"