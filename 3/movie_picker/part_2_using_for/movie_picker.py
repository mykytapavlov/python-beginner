GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}


CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}


if __name__ == '__main__':
    print('Tasks 16. Movie picker: using `for`')
    
    # create ACTORS dictionary from CAST first
    ACTORS = {}
    for movie, actors in CAST.items():
        for actor in actors:
            if actor not in ACTORS:
                ACTORS[actor] = []
            if movie not in ACTORS[actor]:
                ACTORS[actor].append(movie)

    # keep unchanged (as in task 15)
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
