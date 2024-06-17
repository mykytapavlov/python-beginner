from apple import Apple


class Snake:
    def __init__(self, symbols=None, position=(1, 1)):
        if symbols is None:
            self.symbols = {
                'head': '%',
                'body': 'o',
                'tail': '^'
            }
        self.body = [position]

    def eat(self, apple: Apple):
        self.body.append(apple.position)

    def move(self, position: tuple):
        self.body.append(position)
        self.body.pop(0)

    def choices(self):
        positions = set()
        # take coordinates of the head
        i, j = self.body[-1]
        # four possible moves: left, right, up, down
        positions.add((i, j - 1))
        positions.add((i, j + 1))
        positions.add((i - 1, j))
        positions.add((i + 1, j))
        # filter out snake's body
        positions = positions.difference(set(self.body))
        return positions
