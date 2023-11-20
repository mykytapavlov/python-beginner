if __name__ == '__main__':
    Genres = {
        'comedy': ['Meet the parents', 'Angers Management'],
        'adventures': ['Mummy'],
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': ['Meet Joe Black', 'YSP'],
        'thriller': ['Vanilla Sky'],
        'action': ['Mission impossible']
    }
    ACTORS = {
        'Robert De Niro': ['Meet the Parents'],
        'Ben Stiller': ['Meet the Parents'],
        'Adam Sandler': ['Anger Management'],
        'Jack Nicholson': ['Anger Management'],
        'Brendan Fraser': ['Mummy'],
        'Rachel Weisz': ['Mummy'],
        'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
        'Penelope Cruz': ['Vanilla Sky'],
        'Cameron Diaz': ['Vanilla Sky'],
        'Brad Pitt': ['Meet Joe Black'],
        'Anthony Hopkins': ['Meet Joe Black'],
        'Jeremy Renner': ['Mission Impossible']
    }
    # Search by Genre
    x = input("Search by Genre? {y/n}: ")
    if x == 'y':
        print(f'Available Genres: {Genres.keys()}')
        y = input("Enter Genre: ")
        if y in Genres.keys():
            print(f'Available movies: {Genres[y]}')
            z = input("Enter movie: ")
            if z in Genres[y]:
                print(f'Movie to watch: {z}, Genre: {y}')
            else:
                print('Movie not found')
        else:
            print('Genre not found')
    else:
        print("goodbye!")
    # search by Actor
    x1 = input("Search by Actor? {y/n} ")
    if x1 == 'y':
        print(f'Available Actors: {ACTORS.keys()}')
        y1 = input("Enter Actor: ")
        if y1 in ACTORS.keys():
            print(f'Available movies: {ACTORS[y1]}')
            z1 = input("Enter movie: ")
            if z1 in ACTORS[y1]:
                print(f'Movie to watch: {z1}, Starring: {y1}')
            else:
                print('Movie not found')
        else:
            print('Actor not found')
    else:
        print('GoodBye!')
    # CAST = {
    #     'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    #     'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    #     'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    #     'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    #     'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    #     'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
    # }
