# contact = {
#     'name': None,
#     'email': None,
#     'age': None
# }
#
#
# def validate_name(name):
#     if len(name) > 50:
#         raise ValueError('Name is too large!')
#
#
# def validate_email(email):
#     if '@' not in email or '.' not in email:
#         raise ValueError('Invalid email!')
#
#
# def validate_age(age):
#     try:
#         age = int(age)  # Python will raise ValueError if not numeric
#         if age <= 0:
#             # We ask Python to raise ValueError if <= 0
#             raise ValueError
#     except ValueError:
#         raise ValueError('Invalid age!')
#
class Contact:
    # Contact(name='Jack', email='jack@example.com', age=30)
    def __init__(self, age, email, name):
        if self.validate_age(age):
            self.age = age
        else:
            raise ValueError("Invalid age")
        if self.validate_name(name):
            self.name = name
        else:
            raise ValueError("Name is too long")
        if self.validate_email(email):
            self.email = email
        else:
            raise ValueError("Invalid email!")

    @staticmethod
    def validate_name(name):
        if len(name) <= 50:
            return True

    @staticmethod
    def validate_email(email):
        if '@' in email and '.' in email:
            return True

    def validate_age(self, age):
        if isinstance(age, int) is True:
            return True

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"
