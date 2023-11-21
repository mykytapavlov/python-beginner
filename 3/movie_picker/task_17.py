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
        'Robert De Niro': ['Meet the Parents'],
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

    genre_check = input('Search by Genre(y/n): ').lower()

    if genre_check == 'y':
        print(f'Available Genres: {list(GENRES.keys())}')

        available_genres = list(GENRES.keys())

        while True:
            genre = input("Enter genre: ").lower()

            if genre in available_genres:
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


    elif genre_check == 'n':
        actor_check = input('Search by Actor(y/n): ')
        available_actors = list(ACTORS.keys())
        print("Available Actors:", available_actors)

        while True:
            actor = input("Enter actor: ").title()

            if actor in available_actors:
                movies_1 = ACTORS[actor]
                print(f"Available movies: {movies_1} with {actor}")

                while True:
                    user_movie_actor = input("Enter movie: ").title()

                    if user_movie_actor in movies_1:
                        print(f"Movie to watch: {user_movie_actor}. Starring: {actor}.")
                        break

                    else:
                        print(f"Movie {user_movie_actor} with actor {actor} not found. Please try again.")
                break

            else:
                print(f"Actor {actor} not found. Please try again.")

    else:
        print('Choose at least one to be true - Search by genre or Search be actor')