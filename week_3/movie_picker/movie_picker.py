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
search_genre = input('Search by Genre: ')
if search_genre == 'y':
    print('Available Genres:', list(GENRES.keys()))
    key_genre = input('Enter Genre: ')
    if key_genre in GENRES.keys():
        available_movies_g = GENRES[key_genre]
        print('Available Movies:', available_movies_g)
        is_contain_movie = input('Enter movie: ')
        if is_contain_movie in available_movies_g:
            print('Movie to watch:', is_contain_movie + '.', 'Genre:', key_genre + '.')
        else:
            print('No results found')
    else:
        print('No results found')
elif search_genre == 'n':
    search_actor = input('Search by Actor: ')
    if search_actor == 'y':
        print('Available Actors:', list(ACTORS.keys()))
        key_actor = input('Enter actor: ')
        if key_actor in ACTORS.keys():
            available_movies_a = ACTORS[key_actor]
            print('Available movies:', available_movies_a, 'with', key_actor)
            value_movie_watch = input('Enter movie: ')
            if value_movie_watch in available_movies_a:
                print('Movie to watch:', value_movie_watch + '.', 'Starring:', key_actor + '.')
            else:
                print('No results found')
        else:
            print('No results found')
    else:
        print('No results found')
else:
    print('No results found')

#READY