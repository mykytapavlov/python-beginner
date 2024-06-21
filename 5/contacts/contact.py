class Contact:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.validate()

    def validate(self):
        self.validate_name(self.name)
        self.validate_email(self.email)
        self.validate_age(self.age)

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
                raise ValueError('Invalid age!')
        except ValueError:
            raise ValueError('Invalid age!')

    def __repr__(self):
        return f"Contact(name='{self.name}', email='{self.email}', age={self.age})"
