class Snake:
    def __init__(self, symbol='o', position=(1, 1)):
        self.symbol = symbol
        self.head_symbol = '%'  
        self.body = [position]

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        self.body.append(position)
        self.body.pop(0)

    def choices(self):
        head_i, head_j = self.body[-1]
        possible_moves = {(head_i + 1, head_j), (head_i - 1, head_j), (head_i, head_j + 1), (head_i, head_j - 1)}
        return [move for move in possible_moves if move not in self.body]
