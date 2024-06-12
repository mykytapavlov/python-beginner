from contact import Contact
user1 = Contact()
while True:
    try:
        user1.age = input('enter age: ')
        break
    except ValueError:
        print('age is not OK')

while True:
    try:
        user1.name = input('enter name: ')
        break
    except ValueError:
        print('name is not OK')

while True:
    try:
        user1.email = input('enter email: ')
        break
    except ValueError:
        print('email is not OK')
print(user1.name)
print(user1.age)
print(user1.email)
