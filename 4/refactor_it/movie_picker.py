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

def search(source, source_name='genre'):
    while True:
        print(f'Available {source_name}(s): {source}')
        user_input = input(f"Enter {source_name}: ")
        if user_input in source:
            return user_input
        else:
            print(f"{source_name.capitalize()} '{user_input}' not found. Please try again.")

def movies_by_actors(cast):
    actors = {}
    for movie, actors_list in cast.items():
        for actor in actors_list:
            if actor not in actors:
                actors[actor] = []
            actors[actor].append(movie)
    return actors

while True:
    search_genre = input("Search by Genre? (y/n): ")
    if search_genre.lower() == 'y':
        genre = search(source=list(GENRES.keys()), source_name='genre')
        movie = search(source=GENRES[genre], source_name='movie')
        print(f"Movie to watch: {movie}. Genre: {genre}.")
    elif search_genre.lower() == 'n':
        search_actor = input("Search by Actor? (y/n): ")
        if search_actor.lower() == 'y':
            actors = movies_by_actors(CAST)
            actor = search(source=list(actors.keys()), source_name='actor')
            movie = search(source=actors[actor], source_name='movie')
            print(f"Movie to watch: {movie}. Starring: {actor}.")
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
