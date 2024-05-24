def search(source, source_name):
    print(f'Available {source_name}(s): {source}')
    source_input = input(f"Enter {source_name}: ")
    while source_input not in source:
        print(f"{source_name} {source_input} not found. Please try again.")
        source_input = input(f"Enter {source_name}: ")
    return source_input


def movies_by_actors(cast):
    actors = {}
    for movie, movie_cast in CAST.items():
        for actor in movie_cast:
            if actor in actors:
                actors[actor].append(movie)
            else:
                actors[actor] = [movie]
    return actors


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

    genre_search = input("Search by Genre: ")
    if genre_search == "y":
        chosen_genre = search(list(GENRES.keys()),"Genre")
        chosen_movie = search(GENRES[chosen_genre], "Movie")
        print(f"Movie to watch: {chosen_movie}. Genre: {chosen_genre}")
    elif genre_search == "n":
        actor_search = input("Search by Actor: ")
        if actor_search == "y":
            ACTORS = movies_by_actors(CAST)
            chosen_actor = search(list(ACTORS.keys()), "Actor")
            chosen_movie = search(ACTORS[chosen_actor], "Movie")
            print(f"Movie to watch: {chosen_movie}. Starring: {chosen_actor}")
        else:
            print("Input not supported. Exiting")
    else:
        print("Input not supported. Exiting")
