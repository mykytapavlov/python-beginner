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

#ACTORS = {
#    'Robert De Niro': ['Meet the Parents'],
#    'Ben Stiller': ['Meet the Parents'],
#    'Adam Sandler': ['Anger Management'],
#    'Jack Nicholson': ['Anger Management'],
#    'Brendan Fraser': ['Mummy'],
#    'Rachel Weisz': ['Mummy'],
#    'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
#    'Penelope Cruz': ['Vanilla Sky'],
#    'Cameron Diaz': ['Vanilla Sky'],
#    'Brad Pitt': ['Meet Joe Black'],
#    'Anthony Hopkins': ['Meet Joe Black'],
#    'Jeremy Renner': ['Mission Impossible']
#}

CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

list_all_actors = list(set([item for sublist in [*CAST.values()] for item in sublist]))

#Task Task 17. Part 3. While loop.

search_genre = input('Search by Genre: ')
if search_genre == 'y':
    print('Available Genres:', list(GENRES.keys()))
    key_genre = input('Enter Genre: ')
    while key_genre not in GENRES.keys():
        print('Genre', key_genre, 'not found. Please try again.')
        key_genre = input('Enter Genre: ')
    available_movies_g = GENRES[key_genre]
    print('Available Movies:', available_movies_g)
    is_contain_movie = input('Enter movie: ')
    while is_contain_movie not in available_movies_g:
        print('Movie', is_contain_movie, 'not found. Please try again.')
        is_contain_movie = input('Enter movie: ')
    print('Movie to watch:', is_contain_movie + '.', 'Genre:', key_genre + '.')
elif search_genre == 'n':
    search_actor = input('Search by Actor: ')
    if search_actor == 'y':
        print('Available Actors:', list_all_actors)
        key_actor = input('Enter actor: ')
        while key_actor not in list_all_actors:
            print('Actor', key_actor, 'not found. Please try again.')
            key_actor = input('Enter actor: ')
        actors_movies = [key for key, val in CAST.items() if key_actor in val]
        print('Available movies:', actors_movies, 'with', key_actor)
        movie_watch = input('Enter movie: ')
        while movie_watch not in actors_movies:
            print('Movie', movie_watch, 'with actor', key_actor, 'not found. Please try again.')
            movie_watch = input('Enter movie: ')
        print('Movie to watch:', movie_watch + '.', 'Starring:', key_actor + '.')
    else:
        print('No results found')
else:
    print('No results found')

#READY