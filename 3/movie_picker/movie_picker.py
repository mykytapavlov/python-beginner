GENRE = {
    'comedy': ['Meet the parents', 'Angers Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission impossible']
}
CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
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

if __name__ == '__main__':
    # #   Task 16 BEGIN
    #
    # #   create set of actors from values in CAST
    # set_of_actors = set()
    # for key in CAST:
    #     for value in CAST[key]:
    #         set_of_actors.add(value)
    # #   convert set into list
    # list_of_actors = list(set_of_actors)
    # #   create new dictionary with key from actors and empty value with list type
    # Actors = {key: [] for key in list_of_actors}
    #
    # for actor in list_of_actors:
    #     for key1 in CAST:
    #         if actor in CAST[key1]:
    #             Actors[actor].append(key1)
    #
    # print(f'Actors = {Actors}')
    # #   search by Actor from new Actor dictionary
    #
    # search_actor = input("Search by Actor? {y/n} ")
    # if search_actor == 'y':
    #     print(f'Available Actors: {Actors.keys()}')
    #     selected_actor = input("Enter Actor: ")
    #     if selected_actor in Actors.keys():
    #         print(f'Available movies: {Actors[selected_actor]}')
    #         selected_movie = input("Enter movie: ")
    #         if selected_movie in Actors[selected_actor]:
    #             print(f'Movie to watch: {selected_movie}, Starring: {selected_actor}')
    #         else:
    #             print('Movie not found')
    #     else:
    #         print('Actor not found')
    # else:
    #     print('GoodBye!')
    # #    Task 16 END
    # #   Task 15 Start
    # # Search by GENRE
    # search_by_genre = input("Search by Genre? {y/n}: ")
    # if search_by_genre == 'y':
    #     print(f'Available Genres: {GENRE.keys()}')
    #     selected_genre = input("Enter Genre: ")
    #     if selected_genre in GENRE.keys():
    #         print(f'Available movies: {GENRE[selected_genre]}')
    #         selected_movie = input("Enter movie: ")
    #         if selected_movie in GENRE[selected_genre]:
    #             print(f'Movie to watch: {selected_movie}, Genre: {selected_genre}')
    #         else:
    #             print('Movie not found')
    #     else:
    #         print('Genre not found')
    # else:
    #     print("goodbye!")
    # # search by Actor
    # search_by_actor = input("Search by Actor? {y/n} ")
    # if search_by_actor == 'y':
    #     print(f'Available Actors: {ACTORS.keys()}')
    #     selected_actor = input("Enter Actor: ")
    #     if selected_actor in ACTORS.keys():
    #         print(f'Available movies: {ACTORS[selected_actor]}')
    #         selected_movie = input("Enter movie: ")
    #         if selected_movie in ACTORS[selected_actor]:
    #             print(f'Movie to watch: {selected_movie}, Starring: {selected_actor}')
    #         else:
    #             print('Movie not found')
    #     else:
    #         print('Actor not found')
    # else:
    #     print('GoodBye!')
    # #   Task 15 END

    #   Task 17 Start
    search_by_genre = input("Search by Genre? {y/n}: ")
    if search_by_genre == 'y':
        print(f'Available Genres: {GENRE.keys()}')
        selected_genre = input("Enter Genre: ")
        while selected_genre not in GENRE.keys():
            print(f'Genre {selected_genre} not found. Please try again.')
            selected_genre = input("Enter Genre: ")

        print(f'Available movies: {GENRE[selected_genre]}')

        selected_movie = input("Enter movie: ")
        while selected_movie not in GENRE[selected_genre]:
            print(f'Movie {selected_movie} not found. Please try again.')
            selected_movie = input("Enter movie: ")
        print(f'Movie to watch: {selected_movie}, Genre: {selected_genre}')

    # search by Actor
    search_by_actor = input("Search by Actor? {y/n} ")
    if search_by_actor == 'y':
        print(f'Available Actors: {ACTORS.keys()}')
        selected_actor = input("Enter Actor: ")
        while selected_actor not in ACTORS.keys():
            print(f'Actor {selected_actor} not found. Please try again.')
            selected_actor = input("Enter Actor: ")

        print(f'Available movies: {ACTORS[selected_actor]}')

        selected_movie = input("Enter movie: ")
        while selected_movie not in ACTORS[selected_actor]:
            print(f'Movie {selected_movie} not found. Please try again.')
            selected_movie = input("Enter movie: ")

        print(f'Movie to watch: {selected_movie}, Starring: {selected_actor}')

    # Task 16 - another solution:
    search_by_actor = input("Search by actor {y/n}? ")
    if search_by_actor == 'y':
        set_of_actors = set()
        for key in CAST:
            for value in CAST[key]:
                set_of_actors.add(value)
        print(f'Available actors: {set_of_actors}')
        selected_actor = input("Enter Actor:")
        available_movies = list()
        if selected_actor in set_of_actors:
            for key in CAST:
                for value in CAST[key]:
                    if selected_actor == value:
                        available_movies.append(key)
            print(f"Available movies: {available_movies}")

            selected_movie = input("Enter movie: ")
            if selected_movie in available_movies:
                print(f'Movie to watch: {selected_movie}. Starring: {selected_actor}')
            else:
                print("Movie not found")
        else:
            print("Actor not found")
