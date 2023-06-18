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
search_by_genre = input("Search by Genre? (y/n): ")
if search_by_genre.lower() == 'y':
    print("Available Genres:", list(GENRES.keys()))
    genre = input("Enter genre: ").lower()
    if genre in GENRES:
        movies = GENRES[genre]
        print("Available Movies:", movies)
        movie = input("Enter movie: ")
        if movie in movies:
            print("Movie to watch:", movie + ". Genre:", genre + ".")
        else:
            print("Movie not found.")
    else:
        print("Invalid genre.")
else:
    print("Invalid input. Please try again.")

search_by_genre = input("Search by Genre? (y/n): ")
if search_by_genre.lower() == 'n':
    search_by_actor = input("Search by Actor? (y/n): ")
    if search_by_actor.lower() == 'y':
        print("Available Actors:", list(ACTORS.keys()))
        actor = input("Enter actor: ")
        if actor in ACTORS:
            movies = ACTORS[actor]
            print("Available movies:", movies, "with", actor)
            movie = input("Enter movie: ")
            if movie in movies:
                print("Movie to watch:", movie + ". Starring:", actor + ".")
            else:
                print("Movie not found.")
        else:
            print("Invalid actor.")
    else:
        print("Invalid input. Please try again.")



