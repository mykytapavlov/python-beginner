if __name__ == '__main__':

    list_init = [1, 2, 11, 1, 2, 2, 3]
    res_list = []

    for item in list_init:
        if item not in res_list:
            res_list.append(item)

    res_list.sort()


    print('Unique: ', res_list)
