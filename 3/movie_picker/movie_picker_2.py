from orca.keynames import getKeyName

if __name__ == '__main__':

    search_by_genre = input('Search by genre - print y or n: ')

    search_criteria = None
    selected_genre = None
    selected_actor = None

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

    if search_by_genre == 'y':
        search_criteria = 'genre'
    elif search_by_genre == 'n':
        search_by_actor = input('Search by actor - print y or n: ')
        if search_by_actor == 'y':
            search_criteria = 'actor'
        elif search_by_actor == 'n':
            exit()
        else:
            print('Unknown input')
    else:
        print('Unknown input')

    if search_criteria == 'genre':
        available_genres = list(GENRES.keys())
        print('Available genres: ', available_genres)
        selected_genre = input('Please enter a genre: ')
        movies_by_genre = GENRES.get(selected_genre)
        print('Available movies: ', movies_by_genre)
        selected_movie = input('Please enter movie: ')
        print(f'Movie to watch: {selected_movie}. Genre: {selected_genre}.')
    elif search_criteria == 'actor':
        actors = list(CAST.values())
        actors_list = sum(actors, [])
# take unique values
        unique_actors_list = []
        for item in actors_list:
            if item not in unique_actors_list:
                unique_actors_list.append(item)
        print('Available actors: ', unique_actors_list)
        selected_actor = input('Please enter actor: ')
        res_movie_list = []
        for movie, actors_list in CAST.items():
            if selected_actor in actors_list:
                res_movie_list.append(movie)
        print('Available movies: ', res_movie_list, 'with', selected_actor)
        selected_movie = input('Please enter movie: ')
        print(f'Movie to watch: {selected_movie}. Starring: {selected_actor}')










