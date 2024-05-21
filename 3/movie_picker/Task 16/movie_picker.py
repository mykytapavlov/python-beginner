if __name__ == '__main__':
    print('Task 16. Movie picker Version 2.')
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

    genre_search = input("Search by Genre: ")
    if genre_search == "y":
        print(f"Available Genres: {list(GENRES.keys())}")
        genre = input("Enter genre: ")
        if genre in GENRES.keys():
            print(f"Available Movies: {GENRES[genre]}")
            movie = input("Enter movie: ")
            if movie in GENRES[genre]:
                print(f"Movie to watch: {movie}. Genre: {genre}")
            else:
                print("Movie not found. Exiting")
        else:
            print("Genre not found. Exiting")
    elif genre_search == "n":
        actor_search = input("Search by Actor: ")
        if actor_search == "y":
            actors = list()
            for cast in CAST.values():
                for actor in cast:
                    actors.append(actor)
            actors = list(set(actors))
            print(f"Available Actors: {actors}")
            chosen_actor = input(" Enter actor: ")
            if chosen_actor in actors:
                movies = list()
                for movie, cast in CAST.items():
                    if chosen_actor in cast:
                        movies.append(movie)
                print(f"Available Movies: {movies} with {chosen_actor}")
                movie = input("Enter movie: ")
                if movie in movies:
                    print(f"Movie to watch: {movie}. Starring: {chosen_actor}")
                else:
                    print("Movie not found. Exiting")
            else:
                print("Actor not found. Exiting")
        else:
            print("Input not supported. Exiting")
    else:
        print("Input not supported. Exiting")
