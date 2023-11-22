if __name__ == '__main__':
    print('Tasks 16 Movie picker.')

    GENRES = {
        'comedy': ['Meet The Parents', 'Anger Management'],
        'adventures': ['Mummy'],
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': ['Meet Joe Black'],
        'thriller': ['Vanilla Sky'],
        'action': ['Mission Impossible']
    }

    CAST = {
        'Meet The Parents': ['Robert De Niro', 'Ben Stiller'],
        'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
        'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
        'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
        'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
        'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
    }

    genre_check = input('Search by Genre(y/n): ').lower()

    if genre_check == 'y':
        print(f'Available Genres: {list(GENRES.keys())}')
        genre = input('Enter genre: ').lower()

        if genre in GENRES.keys():
            movies = GENRES[genre]
            print(f'Available Movies: {movies}')
            movie = input('Enter movie: ').title()

            for movie_a in movies:
                if movie.title() == movie_a:
                    print(f'Movie to watch: {movie.title()}. Genre: {genre}')
                    break

    elif genre_check == 'n':
        actor_check = input('Search by Actor(y/n): ')

        if actor_check == 'y':

            cast_a = []
            for sublist in list(CAST.values()):
                for element in sublist:
                    cast_a.append(sublist)
                    cast = []
                    for sublist in cast_a:
                        for element in sublist:
                            cast.append(element)

            set_cast = set(cast)
            print(f'Available Actors: {list(set_cast)}')
            actor = input('Enter actor: ').title()

            for movie, cast in CAST.items():
                if actor in cast:
                    print(f'Available movies: {movie} with {actor}')
                    break

            movie_to_watch = input('Enter movie: ').title()

            if movie_to_watch == movie:
                print(f'Movie to watch: {movie}. Starring: {actor}')

    else:
        exit()