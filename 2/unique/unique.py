if __name__ == '__main__':
    list_var = input("Enter sequence of characters separated by comma: ").split(",")
    set_var = set(list_var)
    set_var_int = lisr_var_int = [eval(i) for i in set_var]
    print(sorted(set_var_int))
    