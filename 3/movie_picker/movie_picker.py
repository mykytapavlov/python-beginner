import self

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

# task 15
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