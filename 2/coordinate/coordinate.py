if __name__ == '__main__':
    x = input("please enter x coordinate: ")
    y = input("please enter y coordinate: ")
    z = input("please enter z coordinate: ")
    coordinate = (x, y, z)
    print(type(coordinate))
    print(f'Coordinate: {coordinate}')
    # or just using print:
    # print(f'Coordinate: {tuple([x, y, z])}')
