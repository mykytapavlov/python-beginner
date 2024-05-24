def search(source: list, source_name):
    print(f'Available {source_name}(s): {source}')
    source_input = input(f"Enter {source_name}: ")
    while source_input not in source:
        print(f"{source_name} {source_input} not found. Please try again.")
        source_input = input(f"Enter {source_name}: ")
    return source_input


def movies_by_actors(cast):
    actors = {}
    for movie, movie_cast in cast.items():
        for actor in movie_cast:
            if actor in actors:
                actors[actor].append(movie)
            else:
                actors[actor] = [movie]
    return actors


def prepare(source: dict, user_age):
    new_source = {}
    forbidden_movies = []
    for ages in PG.keys():
        if user_age < ages:
            for movies in PG[ages]:
                forbidden_movies.append(movies)
    for genre_or_actor, movie_list in source.items():
        new_source[genre_or_actor] = [movie for movie in movie_list if movie not in forbidden_movies]
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
        GENRES = prepare(GENRES, age)
        chosen_genre = search(list(GENRES.keys()), "Genre")
        if len(GENRES[chosen_genre]) > 1:
            chosen_movie = search(GENRES[chosen_genre], "Movie")
            print(f"Movie to watch: {chosen_movie}. Genre: {chosen_genre}")
        else:
            print(f"No movies to watch in genre: {chosen_genre}")
    elif genre_search == "n":
        actor_search = input("Search by Actor: ")
        if actor_search == "y":
            ACTORS = movies_by_actors(CAST)
            ACTORS = prepare(ACTORS, age)
            chosen_actor = search(list(ACTORS.keys()), "Actor")
            if len(ACTORS[chosen_actor]) > 1:
                chosen_movie = search(ACTORS[chosen_actor], "Movie")
                print(f"Movie to watch: {chosen_movie}. Starring: {chosen_actor}")
            else:
                print(f"No movies to watch starring: {chosen_actor}")
        else:
            print("Input not supported. Exiting")
    else:
        print("Input not supported. Exiting")
