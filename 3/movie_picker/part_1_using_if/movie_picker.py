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


if __name__ == '__main__':
    print('Tasks 15. Movie picker: using `if`')
    is_by_genre = input('Search by Genre: ').lower() == 'y'
    if is_by_genre:
        print(f'Available Genres: {list(GENRES.keys())}')
        genre = input('Enter genre: ').strip().lower()
        if genre not in GENRES:
            print(f'Genre {genre} not found. Please try again.')
            exit()

        print(f'Available Movies: {GENRES[genre]}')
        movie = input('Enter movie: ').strip().title()
        if movie not in GENRES[genre]:
            print(f'Movie {movie} not found. Please try again.')
            exit()

        print(f'Movie to watch: {movie}. Genre: {genre}.')
        exit()

    is_by_actor = input('Search by Actor: ').lower() == 'y'
    if not is_by_actor:
        print('Search available by Genre or Actor only. Please try again.')
        exit()

    print(f'Available Actors: {list(ACTORS.keys())}')
    actor = input('Enter actor: ').strip().title()
    if actor not in ACTORS:
        print(f'Actor {actor} not found. Please try again.')
        exit()

    print(f'Available movies: {ACTORS[actor]} with {actor}')
    movie = input('Enter movie: ').strip().title()
    if movie not in ACTORS[actor]:
        print(f'Movie {movie} with actor {actor} not found. Please try again.')
        exit()
    print(f'Movie to watch: {movie}. Starring: {actor}.')
    
