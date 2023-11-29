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

is_genre = input('Search by Genre: ')
if is_genre in ('y', 'Y', 'Yes', 'yes'):
    print(f"Available Genres: {list(GENRES.keys())}")
    genre = input('Enter Genre: ')
    if genre in GENRES.keys():
        print(f"Available movies: {GENRES[genre]}")
        movie = input('Enter Movie: ')
        if movie in GENRES[genre]:
            print(f"Movie to watch: {movie}. Genre: {genre}.")
        else:
            print('Bad movie')
    else:
        print(f"{genre} doesn't exist")
else:
    is_actor = input('Search by Actor: ')
    if is_actor in ('y', 'Y', 'Yes', 'yes'):
        print(f"Available Actors: {list(ACTORS.keys())}")
        actor = input('Enter actor: ')
        if actor in ACTORS.keys():
            print(f"Available movies: {ACTORS[actor]} with {actor}")
            movie = input('Enter Movie: ')
            if movie in ACTORS[actor]:
                print(f"Movie to watch: {movie}. Starring: {actor}.")
