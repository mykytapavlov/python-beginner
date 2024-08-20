import itertools

if __name__ == '__main__':
    print('Tasks 15-17. Movie picker.')
GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

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

# search_by_genre = input("Input: > Search by Genre: ")
# if search_by_genre == 'y':
#     available_genres = GENRES.keys()
#     print(f"Output: Available Genres: {available_genres}")
#
#     user_genre = input("Input: > Enter genre: ")
#     if genre in GENRES:
#         available_movies = GENRES[user_genre]
#         print(f"Output: Available Movies: {available_movies}")
#         user_movie = input("Input: > Enter movie: ")
#         if user_movie in available_movies:
#             print(f"Output: Movie to watch: {user_movie}. Genre: {user_genre}.")
#         else:
#             print("Movie not found. Please try again.")
#
#     else:
#         print('Genre not found. Please try again.')
#
#
# if search_by_genre == 'n':
#     search_by_actor = input("Input: > Search by Actor: ")
#     if search_by_actor == 'y':
#         available_actors = ACTORS.keys()
#         print(f"Output: Available Actors: {available_actors}")
#
#         actor = input("Input: > Enter actor: ")
#         if actor in available_actors:
#             movies = ACTORS[actor]
#             print(f"Output: Available Movies: {movies}")
#
#             user_movie = input("Input: > Enter movie: ")
#             if user_movie in movies:
#                 print(f"Output: Movie to watch: {user_movie}. Actor: {actor}.")

CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

# if search_by_genre == 'n':
#     search_by_cast = input("Input: > Search by Actor: ")
#     if search_by_cast == 'y':
#         all_actors = []
#         for actors_list in CAST.values():
#             all_actors.extend(actors_list)
#
#         print(f"Output: Available Actors: {all_actors}")
#
#         actor = input("Input: > Enter actor: ")
#         available_movies=[]
#         for movie, actors_list in CAST.items():
#             if actor in actors_list:
#                 available_movies.append(movie)
#
#         print(f"Available movies: {available_movies} with {actor}")
#         user_movie = input("Input: > Enter movie: ")
#         print(f"Available movies: {available_movies} with {actor}")
#         if user_movie in available_movies:
#             print(f"Output: Movie to watch: {user_movie}. Starring: {actor}.")

while True:
    search_by_genre = input("Input: > Search by Genre: ")
    if search_by_genre == 'y':
        print(f"Output: Available Genres: {list(GENRES.keys())}")
        while True:
            genre = input("Input: > Enter genre: ")
            if genre in GENRES.keys():
                print(f"Output: Available Movies: {GENRES[genre]}")
                while True:
                    movie = input("Input: > Enter movie: ")
                    if movie in GENRES[genre]:
                        print(f"Output: Movie to watch: {movie}. Genre: {genre}.")
                        break
                    else:
                        print(f"Movie [{movie}] not found. Please try again. Available Movies: {GENRES[genre]}.")
                break
            else:
                print(f'Genre [{genre}] not found. Please try again. Available Genres: {list(GENRES.keys())}.')
        break
    elif search_by_genre == 'n':
        search_by_actor = input("Input: > Search by Actor: ")
        if search_by_actor == 'y':
            print(f"Output: Available Actors: {list(ACTORS.keys())}")
            while True:
                actor = input("Input: > Enter actor: ")
                if actor in ACTORS.keys():
                    print(f"Output: Available Movies: {ACTORS[actor]}")
                    while True:
                        movie = input("Input: > Enter movie: ")
                        if movie in ACTORS[actor]:
                            print(f"Output: Movie to watch: {movie}. Actor: {actor}.")
                            break
                        else:
                            print(f"Output: Actor movie [{movie}] not found! Available Actors: {list(ACTORS.keys())}")
                    break
                else:
                    print(f"Output: Actor [{actor}] not found! Available Actors: {list(ACTORS.keys())}")
            break
        else:
            print(f'You entered [{search_by_actor}] which is wrong answer! Available answers are [y] or [n].')
    else:
        print(f'You entered [{search_by_genre}] which is wrong answer! Available answers are [y] or [n].')
