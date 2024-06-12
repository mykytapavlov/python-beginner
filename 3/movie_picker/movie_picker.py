ACTORS = {
    'Robert De Niro': ['Meet the Parents'],
    'Ben Stiller': ['Meet the Parents'],
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
CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}
GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}
PG = {
    13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
    16: {'Vanilla Sky'}
}


def filter_cast(movies_list, age_movies_mapping, users_age):
    filtered_movies_for_cast = []
    new_cast_dict = {}
    for age, b_movies in age_movies_mapping.items():
        for b_movie in b_movies:
            if users_age >= age:
                filtered_movies_for_cast.append(b_movie)
    for cast_movie, cast_actors in movies_list.items():
        if cast_movie in filtered_movies_for_cast:
            new_cast_dict.update({cast_movie: cast_actors})
            #new_cast_dict[cast_movie] = cast_actors
    return new_cast_dict


def filter_movies_by_age(movies_list, age_movies_mapping, users_age):
    filtered_movies = []
    new_list = {}
    for age, b_movies in age_movies_mapping.items():
        for b_movie in b_movies:
            if users_age >= age:
                filtered_movies.append(b_movie)
    for c_genre, c_movies in movies_list.items():
        for c_movie in c_movies:
            if c_movie in filtered_movies:
                #new_list.update({c_genre: c_movies})
                if c_genre in new_list:
                    new_list[c_genre].append(c_movie)
                else:
                    new_list[c_genre] = [c_movie]
    # for d_genre, d_movies in new_list.items():
    #     for d_movie in d_movies:
    #         if d_movie not in filtered_movies:
    #             new_list[d_genre].remove(d_movie)
    return new_list


def search(source, source_name):
    print(f'Available {source_name}: {source}')


def correct_user_input(place_to_compare, search_type):
    user_input = input(f'Enter {search_type}: ')
    while user_input not in place_to_compare:
        print(f'{search_type} {user_input} not found. Please try again.')
        user_input = input(f'Enter {search_type}: ')
    else:
        return user_input


def find_movie_and_actor(place_to_look_in):
    new_list = []
    for item_in_list_one in place_to_look_in:
        for under_item in item_in_list_one:
            if under_item not in new_list:
                new_list.append(under_item)
    return new_list


while True:
    users_age = input('Enter your age: ')
    try:
        users_age = int(users_age)
        break
    except ValueError:
        print("You must enter an integer.")

new_genres = filter_movies_by_age(GENRES, PG, users_age)
new_actors = filter_movies_by_age(ACTORS, PG, users_age)
new_cast = filter_cast(CAST, PG, users_age)

users_choice_for_genre = input('Search by Genre y/n: ')
if users_choice_for_genre == 'y':
    # 'search' function prints out available Genres
    search(list(new_genres.keys()), 'Genres')
    # 'correct_user_input' function takes user's input for genres and compares it with available genres. Repeats if doesn't match
    users_genre_input = correct_user_input(GENRES.keys(), 'Genre')

    # if user's input exists in available genres, we display all movies for the entered genre
    for genre in new_genres:
        if users_genre_input in genre:
            # 'search' function prints out available Movies
            search(new_genres[genre], 'Movies')
            # 'correct_user_input' function takes user's input for movies and compares it with available movies. Repeats if doesn't match
            users_movie_input = correct_user_input(GENRES[genre], 'Movie')
            # if user's input exists in available movies, we display it as a movie to watch with name and genre. Program ends
            for movie in new_genres[genre]:
                if users_movie_input in movie:
                    print(f'Movie to watch: {movie}. Genre: {users_genre_input}.')

if users_choice_for_genre == 'n':
    users_choice_for_actor = input('Search by Actor y/n: ')
    if users_choice_for_actor == 'y':
        # 'find_movie_and_actor' function creates a list with non-repeatable Actors
        available_actors = find_movie_and_actor(new_cast.values())
        # 'search' function prints out available Actors
        search(available_actors, 'Actors')
        # 'correct_user_input' function takes user's input for actors and compares it with available actors. Repeats if doesn't match
        users_actor_input = correct_user_input(available_actors, 'Actor')
        if users_actor_input in available_actors:
            # if user's actor input exists in available actors, we display all available movies for the chosen actor
            available_movies = []
            for movie, actor in new_cast.items():
                if users_actor_input in actor:
                    available_movies.append(movie)
            print(f'Available Movies: {available_movies} with {users_actor_input}')
            # 'correct_user_input' function takes user's input for a movies and compares it with available movies for chosen actor. Repeats if doesn't match
            enter_movie_input = correct_user_input(available_movies, 'Movie')
            # if movie exists in available movies for chosen actor, we display it as a movie to watch with name and actor. Program ends
            if enter_movie_input in available_movies:
                print(f'Movie to watch: {enter_movie_input}. Starring: {users_actor_input}')
    if users_choice_for_actor == 'n':
        print('Good Bye')
