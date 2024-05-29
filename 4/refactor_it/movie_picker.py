def search(source: list, source_name):
    if source:
        print(f'Available {source_name}(s): {source}')
        source_input = input(f"Enter {source_name}: ")
        while source_input not in source:
            print(f"{source_name} {source_input} not found. Please try again.")
            source_input = input(f"Enter {source_name}: ")
    else:
        source_input = "Nothing"
    return source_input


def movies_by_actors(cast):
    new_actors = {}
    for movie, movie_cast in cast.items():
        for actor in movie_cast:
            if actor in new_actors:
                new_actors[actor].append(movie)
            else:
                new_actors[actor] = [movie]
    return new_actors


def prepare(source: dict, user_age):
    new_source = {}
    forbidden_movies = []
    for pg_age in PG:
        if user_age < pg_age:
            for movie in PG[pg_age]:
                forbidden_movies.append(movie)
    for key, value in source.items():
        new_source[key] = [movie for movie in value if movie not in forbidden_movies]
    return new_source


if __name__ == '__main__':
    print('Tasks 18. Movie picker 2.')
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

    PG = {
        13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
        16: {'Vanilla Sky'}
    }

    age = input("Enter your age: ")
    while isinstance(age, int) is False:
        try:
            age = int(age)
        except ValueError:
            age = input("Incorrect input. Try again: ")
    genre_search = input("Search by Genre: ")
    if genre_search == "y":
        genres = prepare(GENRES, age)
        chosen_genre = search(list(genres.keys()), "Genre")
        chosen_movie = search(genres[chosen_genre], "Movie")
        print(f"Movie to watch: {chosen_movie}. Genre: {chosen_genre}")
    elif genre_search == "n":
        actor_search = input("Search by Actor: ")
        if actor_search == "y":
            actors = movies_by_actors(CAST)
            actors = prepare(actors, age)
            chosen_actor = search(list(actors.keys()), "Actor")
            chosen_movie = search(actors[chosen_actor], "Movie")
            print(f"Movie to watch: {chosen_movie}. Starring: {chosen_actor}")
        else:
            print("Input not supported. Exiting")
    else:
        print("Input not supported. Exiting")
