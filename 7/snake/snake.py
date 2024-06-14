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
