if __name__ == '__main__':
    list_var = input("Enter sequence of characters separated by comma: ").split(",")
    list_length = len(list_var)
    half_var = list_length // 2
    print(f'List separated in 2 parts: {list_var[0:half_var]} and {list_var[half_var:]}')
