if __name__ == '__main__':
    print('Tasks 15-17. Movie picker.')
GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
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
start=input('Search by Genre: ')
if start=='y':
    print(f'Available genres {GENRES.keys()}')
    g=input("Enter genre: ")
    if g in GENRES.keys():
        print('Available movies', GENRES[g])
        m=input("Enter movie: ")
        if m in GENRES[g]:
            print(f"Movie to watch: {m}. Genre: {g}")
        else:
            print('The movie was not found, try ones more ')
    else:
        print('The genre was not found, try ones more ')

elif start=='n':
    next=input('Search by actor: ')
    if next=='y':
        print(f'Available actors: {ACTORS.keys()}')
        a=input("Enter actor: ")
        if a in ACTORS.keys():
            print(f'Available movies: {ACTORS[a]} with {a}')
            m=input('Enter movie: ')
            if m in ACTORS[a]:
                print(f"Movie to watch: {m}. Starring: {a}")
            else:
                print('The movie was not found, try ones more')
        else:
            print('The actor was not found, try ones more')
    else:
        print('I cannot help you, see you next time')
else:
    print('Wrong input, try y or n')