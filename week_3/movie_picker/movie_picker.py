
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
search=input("Search by Genre: ")
if search == 'y':
    genre_keys=list(GENRES.keys())
    print(f"Available Genres:", str(genre_keys).strip('[]'))

    search_genre = input("Enter genre: ")
    if search_genre in GENRES.keys():
        genre_movies=str(GENRES[search_genre])
        print("Available movies: ", genre_movies.strip('[]'))

        movie_g = input("Enter movie: ")
        if movie_g in genre_movies:
            print("Movie to watch: ", movie_g.title(), ". Genre: ", search_genre.title())
        else:
            print(f"{movie_g} not found in the list")
    else:
        print(f"{search_genre} not found in the list")
else:
    search_actors = input("Search by Actors: ")
    if search_actors == 'y':
        actors_keys=list(ACTORS.keys())
        print("Available Actors:", str(actors_keys).strip('[]'))

        actors = input("Enter actor: ")
        if actors in ACTORS.keys():
            actor_movies = list(ACTORS[actors])
            print("Available movies: ", str(actor_movies).strip('[]'))

            movie = input("Enter movie: ").title()
            if movie in actor_movies:
                print("Movie to watch: ",movie.title(), ". Starring: ",actors.title() )
            else:
                print(f"{movie} not found in the list")
        else:
            print(f"{actors} not found in the list")
    else:
        print("Search was not successful. Please start the program again to repiet your try.")