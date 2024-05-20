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
CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

# task 16
user_input_genre = input('Search by Genre y/n: ')
if user_input_genre == 'y':
    print('Available Genres: ', list(GENRES.keys()))
    enter_genre_input = input('Enter genre: ')
    for genre in GENRES:
        if enter_genre_input in genre:
            print('Available Movies: ', GENRES.get(genre))
            enter_input_movie = input('Enter movie: ')
            for movie in GENRES.get(genre):
                if enter_input_movie in movie:
                    print('Movie to watch:', movie + '.', 'Genre:', enter_genre_input + '.')
if user_input_genre == 'n':
    user_input_actor = input('Search by Actor y/n: ')
    if user_input_actor == 'y':
        available_actors = []
        for actor in CAST.values():
            for x in actor:
                available_actors.append(x)
        print('Available Actors:', available_actors)
    enter_actor_input = input('Enter actor: ')
    available_movies = []
    for another_movie, another_actor in CAST.items():
        if enter_actor_input in another_actor:
            available_movies.append(another_movie)
    print('Available movies:', available_movies, 'with', enter_actor_input)
    enter_movie_input = input('Enter movie: ')
    for different_movie in available_movies:
        if enter_movie_input in different_movie:
            print('Movie to watch:', different_movie + '.', 'Starring:', enter_actor_input + '.')

# task 15
'''
user_input_genre = input('Search by Genre y/n: ')
if user_input_genre == 'y':
    print('Available Genres: ', list(GENRES.keys()))
    enter_genre_input = input('Enter genre: ')
    if enter_genre_input in GENRES.keys():
        print('Available Movies: ', GENRES[enter_genre_input])
        enter_input_movie = input('Enter movie: ')
        if enter_input_movie in GENRES.get(enter_genre_input):
            print('Movie to watch:', enter_input_movie + '.', 'Genre:', enter_genre_input + '.')
if user_input_genre == 'n':
    user_input_actor = input('Search by Actor y/n: ')
    if user_input_actor == 'y':
        print('Available Actors: ', list(ACTORS.keys()))
        enter_actor_input = input('Enter actor: ')
        if enter_actor_input in ACTORS.keys():
            print('Available movies: ', ACTORS[enter_actor_input], 'with', enter_actor_input)
            enter_movie_input = input('Enter movie: ')
            if enter_movie_input in ACTORS.get(enter_actor_input):
                print('Movie to watch:', enter_movie_input + '.', 'Starring:', enter_actor_input)
'''

# my own solution
'''
user_input = input('Enter Genre or Actor: ')

for genre in GENRES:
    i = 0
    while i < len(GENRES):
        i += 1
        if user_input in genre:
            print(genre, ' :', GENRES.get(genre))
            break

for actor in ACTORS:
    i = 0
    while i < len(ACTORS):
        i += 1
        if user_input in actor:
            print(actor, ' :', ACTORS.get(actor))
            break
'''
