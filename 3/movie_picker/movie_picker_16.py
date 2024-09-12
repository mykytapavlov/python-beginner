if __name__ == '__main__':
    print('Tasks 16. Movie picker.')

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
y = str(input("Enter Genre : "))
if y in GENRES:
    print("Available Movies : ", GENRES[y])
z = str(input("Enter movie : "))
if z in GENRES[y]:
    print("Movie to watch: ", z, "Genre : ", y)

# serach based on actors
act_x = str(input("Search by Genres : "))
act_b = str(input("Search by Actor : "))
new_actors = set()
for actors in CAST.values():
    new_actors.update(actors)
print("Available Actors : ", new_actors)
act_y = str(input("Enter Actor: "))
found_movies = []
for movie, actors in CAST.items():
    if act_y in actors:
        found_movies.append(movie)
print("Available Movies : ", found_movies, "with", act_y)
act_z = str(input("Enter movie : "))
print("Movie to watch: ", act_z, "Starring : ", act_y)
