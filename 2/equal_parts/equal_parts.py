if __name__ == '__main__':
    import numpy as np

    my_list = [3, 2, 1, 4, 5,  2, 'ss', 'q']
    new_list = np.array_split(my_list, 2)




#    def chunks(iterable, size):
#        iterator = iter(iterable)

#    my_list = [3, 2, 1, 4, 5,  2, 'ss', 'q']
#    new_list = list(chunks(my_list, 2))

    print(new_list)
