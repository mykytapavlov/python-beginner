if __name__ == '__main__':
    print('Tasks 15 Movie picker.')

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

        genre = input('Enter genre: ').lower()
        if genre in GENRES.keys():
            movies = GENRES[genre]
            print(movies)
            movie = input('Enter movie: ')

            if str(movie).title() in movies:
                print(f'Movie to watch: {movie.title()}. Genre: {genre}')


    elif genre_check == 'n':
        actor_check = input('Search by Actor(y/n): ')

        if actor_check == 'y':
            print(f'Available Actors: {list(ACTORS.keys())}')
            actor = input('Enter actor: ').title()

            if actor in ACTORS.keys():
                movies_1 = ACTORS[actor]
                print(movies_1)
                movie = input('Enter movie: ')

                if str(movie).title() in movies_1:
                    print(f'Movie to watch: {movie.title()}. Starring: {actor.title()}')

    else:
        exit()
