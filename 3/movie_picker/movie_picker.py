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
#ACTORS = {
  #  'Robert De Niro': ['Meet the Parents'],
  #  'Ben Stiller': ['Meet the Parents'],
  #  'Adam Sandler': ['Anger Management'],
  #  'Jack Nicholson': ['Anger Management'],
  #  'Brendan Fraser': ['Mummy'],
  #  'Rachel Weisz': ['Mummy'],
  #  'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
  #  'Penelope Cruz': ['Vanilla Sky'],
  #  'Cameron Diaz': ['Vanilla Sky'],
  #  'Brad Pitt': ['Meet Joe Black'],
  #  'Anthony Hopkins': ['Meet Joe Black'],
 #   'Jeremy Renner': ['Mission Impossible']
#}
CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
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
        actors=set()
        for actor_list in CAST.values():
            for actor in actor_list:
                actors.add(actor)
        print(f'Available actors: {list(actors)}')

        a=input("Enter actor: ")
        movies= []
        for mov, actor_list in CAST.items():
            if a in actor_list:
                movies.append(mov)
        if movies:
            print(f'Available movies: {movies} with {a}')
            m=input('Enter movie: ')
            if m in movies:
                print(f"Movie to watch: {m}. Starring: {a}")
            else:
                print('The movie was not found, try ones more')
        else:
            print('The actor was not found, try ones more')
    else:
        print('I cannot help you, see you next time')
else:
    print('Wrong input, try y or n')