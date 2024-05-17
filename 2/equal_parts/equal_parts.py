if __name__ == '__main__':
    print('Task 12. Equal parts')
list = input("Enter elements: ").split()
list_1=list[:len(list)//2]
list_2=list[len(list)//2:]
print("First part: ", list_1,"\n","Second part: ", list_2)