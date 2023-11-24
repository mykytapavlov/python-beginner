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
        actors = {}
        for movie, actor_list in CAST.items():
            for actor in actor_list:
                if actor not in actors:
                    actors[actor] = []
                actors[actor].append(movie)

        print(f'Available Actors: {list(actors.keys())}')
        actor = input('Enter actor: ').title()

        if actor in actors:
            movies_with_actor = actors[actor]
            print(f'Available movies: {movies_with_actor}')
            movie_to_watch = input('Enter movie: ').title()

            if movie_to_watch in movies_with_actor:
                print(f'Movie to watch: {movie_to_watch}. Starring: {actor}')

    genre_check = input('Search by Genre(y/n): ').lower()
    if genre_check == 'y':
        search_by_genre()

    elif genre_check == 'n':
        actor_check = input('Search by Actor(y/n): ')

        if actor_check == 'y':
            search_by_actor()

    else:
        exit()