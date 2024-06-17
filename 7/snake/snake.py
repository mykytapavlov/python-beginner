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
        x, y = self.body[-1]
        # four possible moves: left, right, up, down
        positions.add((x, y - 1))
        positions.add((x, y + 1))
        positions.add((x - 1, y))
        positions.add((x + 1, y))
        # filter out snake's body
        positions = positions.difference(set(self.body))
        return positions
