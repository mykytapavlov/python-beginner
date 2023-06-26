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
    13: ['Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'],
    16: ['Vanilla Sky']
}

def search_genre(genre, pg_rate):
    if genre in GENRES:
        if int(pg_rate) >= 13:
            return {key: value for key, value in GENRES.items() if genre == key and key not in PG.get(13, [])}
        elif int(pg_rate) >= 16:
            return {key: value for key, value in GENRES.items() if genre == key and key not in PG.get(16, [])}
    else:
        print("Genre", genre, "not found. Please try again.")

def search_movie(movie, available_movies, source_name):
    if movie in available_movies:
        if source_name == 'genre':
            print('Movie to watch:', movie, "Genre:", genre)
        elif source_name == 'actor':
            print('Movie to watch:', movie, "Starring:", actor)
    else:
        print("Movie", movie, "not found. Please try again.")

def search_actor(actor, available_actors):
    return {key: value for key, value in CAST.items() if actor in value}

search_by_genre = input('Search by Genre? y/n: ')
if search_by_genre == 'y':
    print('Available Genres:', list(GENRES.keys()))
    genre = input('Enter genre: ')
    age = input('Enter your age: ')
    available_movies = search_genre(genre, age)
    if available_movies:
        print('Available Movies:', list(available_movies.values()))
        movie = input('Enter movie: ')
        search_movie(movie, list(available_movies.values()), 'genre')
    else:
        print("Something went wrong. Please try again.")
elif search_by_genre == 'n':
    search_by_actor = input('Search by Actor? y/n: ')
    if search_by_actor == 'y':
        available_actors = list(set([actor for actors in CAST.values() for actor in actors]))
        print('Available Actors:', available_actors)
        actor = input('Enter actor: ')
        available_movies = search_actor(actor, available_actors)
        if available_movies:
            print('Available Movies:', list(available_movies.keys()))
            movie = input('Enter movie: ')
            search_movie(movie, list(available_movies.keys()), 'actor')
        else:
            print("Something went wrong. Please try again.")
    else:
        print("Something went wrong. Please try again.")
else:
    print("Something went wrong. Please try again.")
