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


#ACTORS = {
#    'Robert De Niro': ['Meet the Parents'],
#    'Ben Stiller': ['Meet the Parents'],
#    'Adam Sandler': ['Anger Management'],
#    'Jack Nicholson': ['Anger Management'],
#    'Brendan Fraser': ['Mummy'],
#    'Rachel Weisz': ['Mummy'],
#    'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
#    'Penelope Cruz': ['Vanilla Sky'],
#    'Cameron Diaz': ['Vanilla Sky'],
#    'Brad Pitt': ['Meet Joe Black'],
#    'Anthony Hopkins': ['Meet Joe Black'],
#    'Jeremy Renner': ['Mission Impossible']
#}


CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

search_by_genre = input("Search by Genre? (y/n): ")
while search_by_genre.lower() != 'y' and search_by_genre.lower() != 'n':
    print("Invalid input. Please try again.")
    search_by_genre = input("Search by Genre? (y/n): ")
if search_by_genre.lower() == 'y':
    print("Available Genres:", list(GENRES.keys()))
    genre = input("Enter genre: ").lower()
while genre.lower() not in GENRES:
        print("Genre", genre, "not found. Please try again.")
        genre = input("Enter genre: ")
if genre in GENRES:
        movies = GENRES[genre]
        print("Available Movies:", movies)
        movie = input("Enter movie: ")
while movie not in movies:
            print("Movie", movie, "not found. Please try again.")
            movie = input("Enter movie: ")
if movie in movies:
            print("Movie to watch:", movie + ". Genre:", genre + ".")


#search_by_genre = input("Search by Genre? (y/n): ")
#if search_by_genre.lower() == 'n':
#    search_by_actor = input("Search by Actor? (y/n): ")
#   if search_by_actor.lower() == 'y':
#        print("Available Actors:", list(ACTORS.keys()))
#        actor = input("Enter actor: ")
#        if actor in ACTORS:
#            movies = ACTORS[actor]
#            print("Available movies:", movies, "with", actor)
#            movie = input("Enter movie: ")
#            if movie in movies:
#                print("Movie to watch:", movie + ". Starring:", actor + ".")
#            else:
#                print("Movie not found.")
#        else:
#            print("Invalid actor.")
#    else:
#        print("Invalid input. Please try again.")

search_by_genre = input("Search by Genre? (y/n): ")
if search_by_genre.lower() == 'n':
    search_by_actor = input("Search by Actor? (y/n): ")
    while search_by_actor.lower() != 'y' and search_by_actor.lower() != 'n':
        print("Invalid input. Please try again.")
        search_by_actor = input("Search by Actor? (y/n): ")
    if search_by_actor.lower() == 'y':
        actors = set(actor for movie in CAST for actor in CAST[movie])
        print("Available Actors:", list(actors))
        actor = input("Enter actor: ")
        while actor not in actors:
            print("Actor", actor, "not found. Please try again.")
            actor = input("Enter actor: ")
        movies = [movie for movie in CAST if actor in CAST[movie]]
        if movies:
            print("Available movies:", movies, "with", actor)
            movie = input("Enter movie: ")
            while movie not in movies:
                print("Movie", movie, "with actor", actor, "not found. Please try again.")
                movie = input("Enter movie: ")
            if movie in movies:
                print("Movie to watch:", movie + ". Starring:", actor + ".")
            else:
                print("Movie not found.")
        else:
            print("No movies found for", actor)
    else:
        print("Invalid input. Please try again.")




