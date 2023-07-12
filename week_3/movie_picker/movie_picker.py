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
#Task 15.   Part 1. If statement.
#search based on Genre
key_genre = input('Search by Genre: ')
if key_genre in GENRES.keys():
    # ??? print('Available Genres: ', GENRES.keys())
    print('Available Genres: ', ['comedy', 'adventures', 'romantic', 'drama', 'thriller', 'action'])
else:
    print('No results found')

key_genre = input('Enter Genre: ')
if key_genre in GENRES:
    print('Available Movies: ', GENRES[key_genre])
else:
    print('No results found')

value_movie = input('Enter movie: ')
founding_genres = []
for genres, movies in GENRES.items():
    if value_movie in movies:
        founding_genres.append(genres)
#print(len(founding))
if len(founding_genres) > 0:
    print('Movie to watch: ', value_movie + '.', 'Genre: ', founding_genres)
else:
    print('No results found')

#search based on Actor
key_actor = input('Search by Actor: ')
if key_actor in ACTORS.keys():
    # ???  print('Available Actors: ', ACTORS.keys())
    print('Available Actors: ', ['Robert De Niro', 'Ben Stiller', 'Adam Sandler', 'Jack Nicholson', 'Brendan Fraser',
                                 'Rachel Weisz', 'Tom Cruise', 'Penelope Cruz', 'Cameron Diaz', 'Brad Pitt',
                                 'Anthony Hopkins', 'Jeremy Renner'])
else:
    print('No results found')

key_actor = input('Enter actor: ')
if key_actor in ACTORS.keys():
    print('Available movies: ', ACTORS[key_actor], 'with', key_actor)
else:
    print('No results found')

value_movie_watch = input('Enter movie: ')
founding_actors = []
for key_actors, watch_movies in ACTORS.items():
    if value_movie_watch in watch_movies:
        founding_actors.append(key_actors)
if len(founding_actors) > 0:
    print('Movie to watch: ', value_movie_watch + '.', 'Starring: ', founding_actors)
else:
    print('No results found')