if __name__ == '__main__':
    print('Task 6. String words')
    text = input("Enter your text: ")
    print("These are the words in your text:")
    words = text.split()
    for word in words:
        print(word)
