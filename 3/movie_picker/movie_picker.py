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


# task 17

def search(source, source_name):
    print(f'Available {source_name} : {source}')


users_choice_for_genre = input('Search by Genre y/n: ')
if users_choice_for_genre == 'y':
    search(list(GENRES.keys()), 'Genres')

    users_genre_input = input('Enter genre: ')
    # when user's genre input doesn't match any of genres in GENRES, it goes back and asks to provide a genre again

    while users_genre_input not in GENRES.keys():
        print(f'Genre {users_genre_input} not found. Please try again.')
        users_genre_input = input('Enter genre: ')
    # if user's input is the same as we have in GENRES, we move forward
    if users_genre_input in GENRES.keys():
        # and display all movies for the entered genre
        for genre in GENRES:
            if users_genre_input in genre:
                search(GENRES[genre], 'Movies')
                users_movie_input = input('Enter movie: ')
                # when user's movie input doesn't match any of movie from the list, it goes back and asks to provide a movie again
                while users_movie_input not in GENRES[genre]:
                    print(f'Movie {users_movie_input} not found. Please try again.')
                    users_movie_input = input('Enter movie: ')
                else:
                    # if movie exists in the list, we move on and display it as a movie to watch with name and genre. Program ends
                    for movie in GENRES[genre]:
                        if users_movie_input in movie:
                            print(f'Movie to watch: {movie}. Genre: {users_genre_input}.')

if users_choice_for_genre == 'n':
    users_choice_for_actor = input('Search by Actor y/n: ')
    # when user selects yes for actors we display all available actors
    if users_choice_for_actor == 'y':
        available_actors = []
        # And actors shouldn't repeat
        for actors in CAST.values():
            for actor in actors:
                if actor not in available_actors:
                    available_actors.append(actor)
        search(available_actors, 'Actors')

        users_actor_input = input('Enter actor: ')
        # when user's actor input doesn't match any of actors in CAST, it goes back and asks to provide an actor again
        while users_actor_input not in available_actors:
            print('Actor', users_actor_input, 'not found. Please try again.')
            users_actor_input = input('Enter actor: ')
        if users_actor_input in available_actors:
            # if user's actor input is the same as we have in CAST, we move forward and display all available movies for the chosen actor
            available_movies = []
            for movie, actor in CAST.items():
                if users_actor_input in actor:
                    available_movies.append(movie)
            print(f'Available Movies: {available_movies} with {users_actor_input}')
            enter_movie_input = input('Enter movie: ')
            # when user's movie input doesn't match any of movie from the list, it goes back and asks to provide a movie again
            while enter_movie_input not in available_movies:
                print(f'Movie {enter_movie_input} not found. Please try again.')
                enter_movie_input = input('Enter movie: ')

            else:
                # if movie exists in the list, we move on and display it as a movie to watch with name and actor. Program ends
                print(f'Movie to watch: {enter_movie_input}. Starring: {users_actor_input}')
        if users_choice_for_actor == 'n':
            print('Good Bye')

