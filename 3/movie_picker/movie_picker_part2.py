# Databases
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

print("Welcome to the movie search program!")

choice = input("Search by Genre (y/n)? ")

if choice == 'y':
    print(f"Available Genres: {list(GENRES.keys())}")
    genre = input("Enter genre: ")
    if genre in GENRES:
        movies = GENRES[genre]
        print(f"Available Movies: {movies}")
        movie = input("Enter movie: ")
        if movie in movies:
            print(f"Movie to watch: {movie}. Genre: {genre}.")
        else:
            print("Invalid movie. Program will end.")
    else:
        print("Invalid genre. Program will end.")
elif choice == 'n':
    print(f"Available Actors: {list(set(actor for actors in CAST.values() for actor in actors))}")
    actor = input("Enter actor: ")
    movies = [movie for movie, actors in CAST.items() if actor in actors]
    if movies:
        print(f"Available movies: {movies} with {actor}")
        movie = input("Enter movie: ")
        if movie in movies:
            print(f"Movie to watch: {movie}. Starring: {actor}.")
        else:
            print("Invalid movie. Program will end.")
    else:
        print("Invalid actor. Program will end.")
else:
    print("Invalid input. Program will end.")
