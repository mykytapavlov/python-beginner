if __name__ == '__main__':
    print('Tasks 17. Movie picker.')

GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

# (!) ACTORS storage does not exist anymore.
# ACTORS = {
#     'Robert De Niro': ['Meet the Parents'],
#     'Ben Stiller': ['Meet the Parents'],
#     'Adam Sandler': ['Anger Management'],
#     'Jack Nicholson': ['Anger Management'],
#     'Brendan Fraser': ['Mummy'],
#     'Rachel Weisz': ['Mummy'],
#     'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
#     'Penelope Cruz': ['Vanilla Sky'],
#     'Cameron Diaz': ['Vanilla Sky'],
#     'Brad Pitt': ['Meet Joe Black'],
#     'Anthony Hopkins': ['Meet Joe Black'],
#     'Jeremy Renner': ['Mission Impossible']
# }


CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

#search based on genres
x = str(input("Search by Genres : "))
print("Available Genres : ", list(GENRES.keys()))
while True:
    y = str(input("Enter Genre : "))
    if y in GENRES:
        print("Available Movies : ", GENRES[y])
        break
    else:
        print('Genre', y, 'not found. Please try again.')
while True:
    z = str(input("Enter movie : "))
    if z in GENRES[y]:
        print("Movie to watch: ", z, "Genre : ", y)
        break
    else:
        print('Movie',z, 'not found. Please try again.')

# serach based on actors
act_x = str(input("Search by Genres : "))
act_b = str(input("Search by Actor : "))
new_actors = set()
for actors in CAST.values():
    new_actors.update(actors)
print("Available Actors : ", new_actors)
while True:
    found_movies = []
    act_y = str(input("Enter actor: "))
    for movie, actors in CAST.items():
        if act_y in actors:
            found_movies.append(movie)
    if found_movies:
        print("Available Movies:", found_movies, "with", act_y)
        break
    else:
        print("Actor", act_y, "not found. Please try again.")
while True:
    act_z = str(input("Enter movie: "))
    if act_z in found_movies:
        print("Movie to watch:", act_z, "Starring:", act_y)
        break
    else:
        print("Movie", act_z, "with actor",act_y, "not found. Please try again")

