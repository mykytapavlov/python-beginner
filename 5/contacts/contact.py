class Contact:
    def __init__(self,name,email,age):
        self._name = self.validate_name(name)
        self._email = self.validate_email(email)
        self._age = self.validate_age(age)

    @classmethod
    def create_from_input(cls):
        name = input('Name: ')
        email = input('Email: ')
        age = input('Age: ')
        return cls(name, email, age)

    @staticmethod
    def validate_name(name):
        if len(name) > 50:
            raise ValueError('Name is too large!')
        else:
            return name

    @staticmethod
    def validate_email(email):
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email!')
        else:
            return email

    @staticmethod
    def validate_age(age):
        try:
            age = int(age)  # Python will raise ValueError if not numeric
            if age <= 0:
                # We ask Python to raise ValueError if <= 0
                raise ValueError
            else:
                return age
        except ValueError:
            raise ValueError('Invalid age!')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = self.validate_name(name)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = self.validate_email(email)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = self.validate_age(age)

    def __str__(self):
        output = ''
        output = (
                output
                + '-' * 10 + '\n'
                + 'Name:' + self.name + '\n'
                + 'Email:' + self.email + '\n'
                + 'Age:' + str(self.age) + '\n'
                + '-' * 10
        )
        return output
