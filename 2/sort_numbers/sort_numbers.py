if __name__ == '__main__':
    list_var = input("Enter sequence of numbers separated by comma: ").split(",")
    lisr_var_int = [eval(i) for i in list_var]
    print(f'Sorted list: {sorted(lisr_var_int)}')
