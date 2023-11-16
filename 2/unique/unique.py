if __name__ == '__main__':
    list_var = input("Enter sequence of characters separated by comma: ").split(",")
    list_var_int = [int(i) for i in list_var]
    set_var = set(list_var_int)
    print(f'Sorted list with unique values: {sorted(set_var)}')
    cnt = dict()
    for word in list_var_int:
        if word in cnt:
            cnt[word] += 1
        else:
            cnt[word] = 1
    print(f'Occurrence of each unique number: {cnt}')
