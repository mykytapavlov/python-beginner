if __name__ == '__main__':
    print('Task 7. String slice')
phrase= input("Enter phrase:")
start=int(input("Enter start index:"))
end = int(input("Enter end index:"))
substring = phrase[start:end]
print(substring)