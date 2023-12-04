def from_cast_to_actors(source: dict):
    actors = {}
    for movie, actors_list in source.items():
        for actor in actors_list:
            if actor not in actors:
                actors[actor] = []
            actors[actor].append(movie)
    return actors


def search_universal(source: dict, source_name: str):
    if source_name == "movie":
        first_var, second_var = "actor", "genre"
    elif source_name == "genre":
        first_var, second_var = "genre", "movie"
    else:
        print("Incorrect request. Nothing found...")
        return 0
    print(f'Available {first_var.capitalize()}: {list(source.keys())}')
    selected_genre = input(f'Enter {first_var}: ')
    while selected_genre not in source.keys():
        print(f'{first_var.capitalize()} {selected_genre} not found. Please try again.')
        selected_genre = input(f'Enter  {first_var}: ')
    print(f'Available movies: {source[selected_genre]}')
    selected_movie = input(f"Enter movie: ")
    while selected_movie not in source[selected_genre]:
        print(f'Movie {selected_movie} not found. Please try again.')
        selected_movie = input(f"Enter movie: ")
    print(f'Movie to watch: {selected_movie}, {first_var.capitalize()}: {selected_genre}')


def search_by_mykyta(source, source_name: str):
    print(f'Available {source_name}: {source}')
    selected_genre = input(f'Enter {source_name}: ')
    while selected_genre not in source:
        print(f'{source_name.capitalize()} {selected_genre} not found. Please try again.')
        selected_genre = input(f'Enter  {source_name}: ')
    return selected_genre


def sort_movies_by_age(source: dict, user_age):
        sorted_movies = []
        for age, movie_list in source.items():
            if age <= user_age:
                for movie in movie_list:
                    sorted_movies.append(movie)
        return sorted_movies


def users_age():
    age = input("Please enter your age: ")
    while True:
        try:
            int(age)
            break
        except (TypeError, ValueError):
            age = input("Please enter your age: ")
    return int(age)


def prepare_genres(source: dict, pg_rate, agedict: dict):
        list_of_allowed_movies = sort_movies_by_age(agedict, pg_rate)
        new_genres = {}
        for genre, movies_list in source.items():
            for movie in movies_list:
                if movie in list_of_allowed_movies:
                    if genre not in new_genres:
                        new_genres[genre] = []
                    new_genres[genre].append(movie)
                # if movie in list_of_allowed_movies:
                #     new_genres[genre].append(movie)
        return new_genres


def prepare_actors(source: dict, pg_rate, agedict: dict):
        list_of_allowed_movies = sort_movies_by_age(agedict, pg_rate)
        new_actors = {}
        for actor, movies_list in source.items():
            for movie in movies_list:
                if movie in list_of_allowed_movies:
                    if actor not in new_actors:
                        new_actors[actor] = []
                    new_actors[actor].append(movie)
        return new_actors
