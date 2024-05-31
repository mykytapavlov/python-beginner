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

while True:
    search_genre = input("Search by Genre? (y/n): ")
    if search_genre == 'y' or search_genre == 'Y':
        while True:
            print("Available Genres:", list(GENRES.keys()))
            genre = input("Enter genre: ")
            if genre in GENRES:
                print("Available Movies:", GENRES[genre])
                while True:
                    movie = input("Enter movie: ")
                    if movie in GENRES[genre]:
                        print(f"Movie to watch: {movie}. Genre: {genre}.")
                        break
                    else:
                        print("Movie", movie, "not found. Please try again.")
                break
            else:
                print("Genre", genre, "not found. Please try again.")
    elif search_genre == 'n' or search_genre == 'N':
        search_actor = input("Search by Actor? (y/n): ")
        if search_actor == 'y' or search_actor == 'Y':
            available_actors = set(actor for movie in CAST for actor in CAST[movie])
            while True:
                print("Available Actors:", list(available_actors))
                actor = input("Enter actor: ")
                if actor in available_actors:
                    movies = [movie for movie, actors in CAST.items() if actor in actors]
                    print("Available movies:", movies, "with", actor)
                    while True:
                        movie = input("Enter movie: ")
                        if movie in movies:
                            print(f"Movie to watch: {movie}. Starring: {actor}.")
                            break
                        else:
                            print("Movie", movie, "with actor", actor, "not found. Please try again.")
                    break
                else:
                    print("Actor", actor, "not found. Please try again.")
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
