raw_file_content = input('Type text: ')
file_content = raw_file_content.lower()
for word in file_content.split():
    print(word)
