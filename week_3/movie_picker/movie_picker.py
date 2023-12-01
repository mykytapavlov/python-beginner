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

available_actors = []
for key, val in CAST.items():
    for i in val:
        available_actors.append(i)

search = input("Search by Genre: ")
if search == 'y':
    genre_keys = list(GENRES.keys())
    print(f"Available Genres:", str(genre_keys).strip('[]'))

    while True:
        search_genre = input("Enter genre: ")
        if search_genre in GENRES.keys():
            print("Available movies: ", str(GENRES[search_genre]))
            break
        else:
            print("Genre", search_genre, " not found. Please try again.")
        continue

    while True:
        movie_name_i = input("Enter movie: ")
        if movie_name_i in GENRES.get(search_genre):
            print("Movie to watch: ", movie_name_i, ". Genre: ", search_genre.title())
            break
        else:
            print("Movie", movie_name_i, " not found. Please try again.")
        continue
else:
    search_actor = input("Search by Actor: ")
    if search_actor == 'y':
        print('Available Actors:', available_actors)
        actor_name = input("Enter actor: ")

        while actor_name not in available_actors:
            print('Actor', actor_name, 'not found. Please try again.')
            actor_name = input('Enter actor: ')
        actor_movies = [key for key, val in CAST.items() if actor_name in val]
        print('Available movies:', actor_movies, 'with', actor_name)
        movie_name = input('Enter movie: ')

        while movie_name not in actor_movies:
            print('Movie', movie_name, 'with actor', actor_name, 'not found. Please try again.')
            movie_watch = input('Enter movie: ')
        print('Movie to watch:', movie_name, '.', 'Starring:', CAST[movie_name], '.')
    else:
        print(f"Restart the program to search again")