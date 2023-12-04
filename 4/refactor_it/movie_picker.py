from test_functions import *


GENRE1 = {
    'comedy': ['Meet the Parents', 'Angers Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission impossible']
}
CAST1 = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}
ACTORS1 = {
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
PG1 = {
    13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
    16: {'Vanilla Sky'}
}
PG = {
    13: {'Meet the Parents', 'Mummy'},
    16: {'Vanilla Sky'}
}


if __name__ == '__main__':
    print('Tasks 18. Movie picker 2.')
    # genre = search_by_mykyta(GENRE1.keys(), "genre")
    # movie = search_by_mykyta(GENRE1[genre], "movie")
    # print(f'Movie to watch : {movie}, Genre: {genre}')
    #
    # new_actors = from_cast_to_actors(CAST1)
    # actor = search_by_mykyta(new_actors.keys(), "actor")
    # movie = search_by_mykyta(new_actors[actor], "movie")
    # print(f'Movie to watch : {movie}, Starring: {actor}')


    var_age = users_age()
    genre2 = prepare_genres(GENRE1, var_age, PG)
    genre = search_by_mykyta(genre2.keys(), "genre")
    movie = search_by_mykyta(genre2[genre], "movie")
    print(f'Movie to watch : {movie}, Genre: {genre}')

    actors2 = prepare_actors(ACTORS1, var_age, PG)
    actor = search_by_mykyta(actors2.keys(), "actor")
    movie = search_by_mykyta(actors2[actor], "movie")
    print(f'Movie to watch : {movie}, Starring: {actor}')
