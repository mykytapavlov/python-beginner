if __name__ == '__main__':
    print('Tasks 18. Movie picker 2. Part 2')

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

    PG = {
        13: {'Meet The Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
        16: {'Vanilla Sky'}
    }


    def movies_by_actors(cast):
        actors = {}
        for movie, actor_list in cast.items():
            for actor in actor_list:
                if actor not in actors:
                    actors[actor] = []
                actors[actor].append(movie)
        return actors

    def prepare(genres, pg_ratings, user_age):
        allowed_movies = set()
        for age_limit, movies in pg_ratings.items():
            if user_age >= age_limit:
                allowed_movies.update(movies)

        new_genres = {genre: list(set(movies) & allowed_movies) for genre, movies in genres.items()}
        return new_genres

    def search(source, source_name):
        while True:
            print(f'Available {source_name}s: {list(source.keys())}')
            search_input = input(f'Enter {source_name}: ').lower()

            if search_input in source:
                items = source[search_input]
                print(f'Available {source_name} items: {items}')

                while True:
                    selected_item = input(f'Enter {source_name} item: ').title()

                    if selected_item in items:
                        print(f'{source_name.title()} to watch: {selected_item}. {source_name.title()}: {search_input}')
                        return
                    else:
                        print(f'Invalid {source_name} item. Try again.')
            else:
                print(f'Invalid {source_name}. Try again.')

    ACTORS = movies_by_actors(CAST)

    try:
        user_age = int(input('Please enter your age: '))
        if not isinstance(user_age, int):
            raise ValueError('Age must be an integer.')

        filtered_genres = prepare(GENRES, PG, user_age)
        filtered_actors = prepare(ACTORS, PG, user_age)

        genre_check = input('Search by Genre(y/n): ').lower()
        if genre_check == 'y':
            search(filtered_genres, 'genre')

        elif genre_check == 'n':
            actor_check = input('Search by Actor(y/n): ')

            if actor_check == 'y':
                search(filtered_actors, 'actor')

        else:
            exit()

    except ValueError as ve:
        print(f"Invalid input: {ve}")
