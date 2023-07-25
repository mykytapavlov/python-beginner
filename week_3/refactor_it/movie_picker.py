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


def cast_to_actors(cast):
    actors_final = {}
    for movie, actors in cast.items():
        for actor in actors:
            if actor in actors_final:
                actors_final[actor].append(movie)
            else:
                actors_final[actor] = [movie]
    return actors_final
# Restructuring the CAST dict into previous ACTORS view


def search(source, source_name='genre'):
    print(f'Available {source_name.capitalize()}(s): {source}')
    user_input = input(f'Enter {source_name.capitalize()}: ')
    while user_input not in source:
        print(f'{source_name.capitalize()} {user_input} not found. Please try again.')
        user_input = input(f'Enter {source_name.capitalize()}: ')
    return user_input
# Ask for an input GENRE and repeat unless match is found


def prepare_genres(genres, pg_rate):
    new_genres = {}
    if pg_rate in range(13, 16):
        for genre, movies in genres.items():
            for movie in movies:
                if movie not in PG[16]:
                    if genre in new_genres:
                        new_genres[genre].append(movie)
                    else:
                        new_genres[genre] = [movie]
    elif pg_rate in range(16, 1000):
            new_genres = genres.copy()
    return new_genres
# Prefilter GENRES based on the PG


def prepare_actors(actors, pg_rate):
    new_actors = {}
    if pg_rate in range(13, 16):
        for actor, movies in actors.items():
            for movie in movies:
                if movie not in PG[16]:
                    if actor in new_actors:
                        new_actors[actor].append(movie)
                    else:
                        new_actors[actor] = [movie]
    elif pg_rate in range(16, 1000):
        new_actors = actors.copy()
    return new_actors
# Prefilter actors based on the PG


def input_pgrate(value):
    while True:
        try:
            value = int(input('Enter your age: '))
            if value < 1 or value > 150:
                raise ValueError
            break
        except ValueError:
            print('Please enter a valid integer age between 1 and 150.')
    return value
# Accept Users input age, only integer up to 150 years


pg_rate = input_pgrate(True)
if pg_rate >= 13:
    user_is = input('Search by Genre: ')
    if user_is == 'y':
        new_genres = prepare_genres(GENRES, pg_rate)
        genre = search(source=list(new_genres.keys()), source_name='genre')
        movie_by_genre = search(source=new_genres[genre], source_name='movie')
        print('Movie to watch:', movie_by_genre + '.', 'Genre:', genre + '.')
    elif user_is == 'n':
        actors = cast_to_actors(CAST)
        new_actors = prepare_actors(actors, pg_rate)
        actor = search(source=list(new_actors.keys()), source_name='actor')
        movie_by_actor = search(source=new_actors[actor], source_name='movie')
        print('Movie to watch:', movie_by_actor + '.', 'Starring:', actor + '.')
    else:
        print('No results found')
else:
    print('You are too young and forbidden to use our service!')


# READY