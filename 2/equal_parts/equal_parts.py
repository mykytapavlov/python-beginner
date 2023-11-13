if __name__ == '__main__':
    print('Task 12. Equal parts')
list = [3, 2, 1, 4, 5,  2, 'ss', 'q', 5]
list_1 = list[:len(list)//2]
list_2 = list[len(list)//2:]
print(list_1, list_2)