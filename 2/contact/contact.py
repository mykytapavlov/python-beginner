if __name__ == '__main__':
    print('Task 14. Contact.')
    contact = dict()
    contact['name'] = input("Enter your name: ")
    contact['age'] = int(input("Enter your age: "))
    contact['address'] = input("Enter your address: ")
    contact['phone'] = int(input("Enter your phone in format 0670000000: "))
    print(f"Contact created: {contact}")
