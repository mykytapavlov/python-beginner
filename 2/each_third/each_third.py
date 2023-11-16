if __name__ == '__main__':
    list_var = input("Enter sequence of characters separated by comma: ").split(",")
    str_var_final = [value.strip() for value in list_var]
    print(f'Each third value in list is: {str_var_final[0::3]}')
