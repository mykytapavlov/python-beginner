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


def search(source, source_name):
    print(f'Available {source_name}(s): {source}')

    while True:
        item = input(f'Enter {source_name}: ')
        if item in source:
            break
        print(f'{source_name} not found. Please try again.')

    return item


def movies_by_actors(cast):
    actors = {}
    for movie, movie_cast in cast.items():
        for actor in movie_cast:
            if actor not in actors:
                actors[actor] = []
            if movie not in actors[actor]:
                actors[actor].append(movie)
    return actors


if __name__ == '__main__':
    print('Tasks 18. Movie picker: using `function`')

    by_genre = input('Search by Genre: ').lower() == 'y'

    if by_genre:
        genre = search(source=list(GENRES.keys()), source_name='genre')
        movie = search(source=GENRES[genre], source_name='movie')
        print(f'Movie to watch: {movie}. Genre: {genre}.')
        exit()

    by_actor = input('Search by Actor: ').lower() == 'y'

    if by_actor:
        actors = movies_by_actors(CAST)
        actor = search(source=list(actors.keys()), source_name='actor')
        movie = search(source=actors[actor], source_name='movie')
        print(f'Movie to watch: {movie}. Starring: {actor}.')
        exit()

    print('Search available by Genre or Actor only. Please try again.')
    
