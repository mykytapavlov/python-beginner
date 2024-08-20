if __name__ == '__main__':
    print('Tasks 18. Movie picker 2.')


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

PG = {
    13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
    16: {'Vanilla Sky'}
}

def movies_by_actors(cast):
    actors = {}
    for movie, cast_list in cast.items():
        for actor in cast_list:
            if actor not in actors:
                actors[actor] = [movie]
            else:
                actors[actor].append(movie)
    return actors

def search(source, source_name='genre'):
    print(f'Available {source_name}(s): {list(source)}')

    while True:
        input_value = input(f"Input: > Enter {source_name}: ")
        if input_value in source:
            return input_value
        else:
            print(f'{source_name} [{input_value}] not found. Please try again. Available {source_name}(s): {list(source)}.')

def prepare(source, pg_rate, user_age):
    available_movies = []
    for rate, movies in pg_rate.items():
        if user_age > rate:
            available_movies = [*available_movies, *movies]

    new_source = {}
    for key, value in source.items():
        for movie in value:
            if movie in available_movies:
                if key not in new_source.keys():
                    new_source[key] = [movie]
                else:
                    new_source[key].append(movie)

    return new_source

user_age = int(input("Enter you age: "))
GENRES = prepare(GENRES, PG, user_age)
actors = prepare(movies_by_actors(CAST), PG, user_age)

while True:
    search_by_genre = input("Input: > Search by Genre: ")
    if search_by_genre == 'y':
        if len(GENRES) == 0:
            print(f"Output: Genres list are empty.")
            break
        genre = search(source=GENRES.keys(), source_name='genre')
        movie = search(source=GENRES[genre], source_name='movie')
        print(f"Output: Movie to watch: {movie}. Genre: {genre}.")
        break
    elif search_by_genre == 'n':
        if len(actors) == 0:
            print(f"Output: Actors list are empty.")
            break

        actor = search(source=actors.keys(), source_name='actor')
        movie = search(source=actors[actor], source_name='movie')
        print(f"Output: Movie to watch: {movie}. Actor: {actor}.")
        break
    else:
        print(f'You entered [{search_by_genre}] which is wrong answer! Available answers are [y] or [n].')
