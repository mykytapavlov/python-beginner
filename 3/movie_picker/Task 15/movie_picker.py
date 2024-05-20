if __name__ == '__main__':
    print('Task 15. Movie picker.')
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
            print(f"Available Actors: {list(ACTORS.keys())}")
            actor = input(" Enter actor: ")
            if actor in ACTORS.keys():
                print(f"Available Movies: {ACTORS[actor]} with {actor}")
                movie = input("Enter movie: ")
                if movie in ACTORS[actor]:
                    print(f"Movie to watch: {movie}. Starring: {actor}")
                else:
                    print("Movie not found. Exiting")
            else:
                print("Actor not found. Exiting")
        else:
            print("Input not supported. Exiting")
    else:
        print("Input not supported. Exiting")
