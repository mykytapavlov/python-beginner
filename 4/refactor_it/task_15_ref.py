if __name__ == '__main__':
    print('Tasks 15 Movie picker. Refactor')

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
        genre = input('Enter genre: ').lower()

        if genre in GENRES:
            movies = GENRES[genre]
            print(f'Available Movies: {movies}')
            movie = input('Enter movie: ').title()

            if movie in movies:
                print(f'Movie to watch: {movie}. Genre: {genre}')

    def search_by_actor():
        print(f'Available Actors: {list(ACTORS.keys())}')
        actor = input('Enter actor: ').title()

        if actor in ACTORS:
            available_movies = ACTORS[actor]
            print(f'Available movies: {available_movies}')
            enter_movie = input('Enter movie: ').title()

            if enter_movie in available_movies:
                print(f'Movie to watch: {enter_movie}. Starring: {actor}')


    genre_check = input('Search by Genre(y/n): ').lower()

    if genre_check == 'y':
        search_by_genre()

    elif genre_check == 'n':
        actor_check = input('Search by Actor(y/n): ')

        if actor_check == 'y':
            search_by_actor()

    else:
        exit()
