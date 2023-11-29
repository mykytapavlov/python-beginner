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

search = input("Search by Genre: ")
if search == 'y':
    genre_keys = list(GENRES.keys())
    print(f"Available Genres:", str(genre_keys).strip('[]'))

    search_genre = input("Enter genre: ")
    if search_genre in GENRES.keys():
        genre_movies = str(GENRES[search_genre])
        print("Available movies: ", genre_movies.strip('[]'))

        movie_g = input("Enter movie: ")
        if movie_g in genre_movies:
            print("Movie to watch: ", movie_g.title(), ". Genre: ", search_genre.title())
        else:
            print(f"{movie_g} not found in the list of genres")
    else:
        print(f"{search_genre} not found in the list of films")
else:
    search_actor = input("Search by Actor: ")

    if search_actor == 'y':
        actor = input("Enter actor: ")
        print(f'Available movies: ')
        for movie, cast in CAST.items():
            if actor in cast:
                print(f'{movie} with {actor}')
            continue

        movie_name = input("Enter movie: ").title()
        for movie, cast in CAST.items():
            if movie_name in movie:
                print("Movie to watch: ", movie_name.title(), ". Starring: ", actor.title())

    else:
        print(f"Restart the program to search again")