class Contact:
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    @classmethod
    def create_from_input(cls):
        name = input('Name: ')
        cls.validate_name(name)
        email = input('Email: ')
        cls.validate_email(email)
        age = input('Age: ')
        cls.validate_age(age)
        return cls(name, email, age)

    @staticmethod
    def validate_name(name):
        if len(name) > 50:
            raise ValueError('Name is too large!')

    @staticmethod
    def validate_email(email):
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email!')

    @staticmethod
    def validate_age(age):
        try:
            age = int(age)  # Python will raise ValueError if not numeric
            if age <= 0:
                # We ask Python to raise ValueError if <= 0
                raise ValueError
        except ValueError:
            raise ValueError('Invalid age!')

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
