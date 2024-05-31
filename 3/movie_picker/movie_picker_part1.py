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
    choice = input("Search by Actor (y/n)? ")
    if choice == 'y':
        print(f"Available Actors: {list(ACTORS.keys())}")
        actor = input("Enter actor: ")
        if actor in ACTORS:
            movies = ACTORS[actor]
            print(f"Available movies: {movies} with {actor}")
            movie = input("Enter movie: ")
            if movie in movies:
                print(f"Movie to watch: {movie}. Starring: {actor}.")
            else:
                print("Invalid movie. Program will end.")
        else:
            print("Invalid actor. Program will end.")
    else:
        print("Invalid choice. Program will end.")
else:
    print("Invalid input. Program will end.")

