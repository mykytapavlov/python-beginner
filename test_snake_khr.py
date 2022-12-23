class Board:
    def __init__(self, width, height, top_border="<", bottom_border=">", vert_border="^"):
        self.top_boarders = top_border
        self.bottom_boarders = bottom_border
        self.vert_boarders = vert_border
        self.width = width
        self.height = height
        self.board = self.new_board()

    def new_board(self):
        new_board = []
        for i in range(self.height):
            if i in {0}:
                row = [self.top_boarders] * self.width
                new_board.append(row)
            elif i in {self.height - 1}:
                row = [self.bottom_boarders] * self.width
                new_board.append(row)
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(self.vert_boarders)
                    else:
                        row.append(" ")
                new_board.append(row)
        return new_board

    def show(self):
        for row in self.board:
            print(' '.join(row))


class Snake:
    def __init__(self, head="@", init_body="o", init_direction=(1, 0), init_position=(1, 1)):
        self.direction = init_direction
        self.body = init_body
        self.position = init_position
        self.head = head

    # def head(self):
    #     return self.body[-1]

    def eat(self, position):
        self.position = position

    def set_direction(self, direction):
        self.direction = direction


class Food(object):
    def __init__(self, location):
        self.location = location


class Game:
    def __init__(self):
        self.board = Board(width=40, height=20)
        self.init_body = [(2, 1), (3, 1), (4, 1), (5, 1)]
        self.snake = Snake(init_body="o", init_direction=(1, 0))
        self.food = Food(location=(10, 10))

    def render(self):
        board = self.board


#

if __name__ == '__main__':
    b = Board(width=40, height=20)
    s = Snake()
    b.show()
