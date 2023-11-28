if __name__ == '__main__':
    print('Tasks 17 Movie picker.')

    GENRES = {
        'comedy': ['Meet The Parents', 'Anger Management'],
        'adventures': ['Mummy'],
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': ['Meet Joe Black'],
        'thriller': ['Vanilla Sky'],
        'action': ['Mission Impossible']
    }

    ACTORS = {
        'Robert De Niro': ['Meet The Parents'],
        'Ben Stiller': ['Meet The Parents'],
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

    def search_by_genre():
        print(f'Available Genres: {list(GENRES.keys())}')

        while True:
            genre = input("Enter genre: ").lower()

            if genre in list(GENRES.keys()):
                movies = GENRES[genre]
                print("Available Movies:", movies)

                while True:
                    movie = input("Enter movie: ").title()

                    if movie in movies:
                        print(f"Movie to watch: {movie}. Genre: {genre}.")
                        break

                    else:
                        print(f"Movie {movie} not found. Please try again.")
                break

            else:
                print(f"Genre {genre} not found. Please try again.")

    def search_by_actor():
        print("Available Actors:", list(ACTORS.keys()))

        while True:
            actor = input("Enter actor: ").title()

            if actor in list(ACTORS.keys()):
                available_movies = ACTORS[actor]
                print(f"Available movies: {available_movies} with {actor}")

                while True:
                    user_movie_actor = input("Enter movie: ").title()

                    if user_movie_actor in available_movies:
                        print(f"Movie to watch: {user_movie_actor}. Starring: {actor}.")
                        break

                    else:
                        print(f"Movie {user_movie_actor} with actor {actor} not found. Please try again.")
                break

            else:
                print(f"Actor {actor} not found. Please try again.")

    genre_check = input('Search by Genre(y/n): ').lower()
    if genre_check == 'y':
        search_by_genre()

    elif genre_check == 'n':
        actor_check = input('Search by Actor(y/n): ')

        if actor_check == 'y':
            search_by_actor()

    else:
        print('Choose at least one to be true - Search by genre or Search be actor')
