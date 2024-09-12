if __name__ == '__main__':

    search_criteria = input('Please enter search criteria - genre or actor: ')

    selected_genre = None
    selected_actor = None

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

    if search_criteria == 'genre':
        selected_genre = input('Please enter a genre: \ncomedy \nadventures \nromantic \ndrama \nthriller \naction \n ')
        movies_by_genre = GENRES.get(selected_genre)
        print('Available movies: ', movies_by_genre)
    elif search_criteria == 'actor':
        selected_actor = input('Please enter an actor: \nRobert De Niro \nBen Stiller \nAdam Sandler \nJack Nicholson \nBrendan Fraser \nRachel Weisz \nTom Cruise \nPenelope Cruz \nCameron Diaz \nBrad Pitt \nAnthony Hopkins \nJeremy Renner \n ')
        movies_by_actor = ACTORS.get(selected_actor)
        print('Available movies: ', movies_by_actor)
    else:
        print('No such a search criteria')


