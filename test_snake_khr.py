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
    def __init__(self, symbol="o", position=(1, 1), head="@"):
        # self.position = None
        self.symbol = symbol
        self.body = [position]
        self.head = head
        # self.head = self.body[-1]

    def eat(self, position: tuple):
        new_body = self.body[0][0] + position[0], self.body[0][1] + position[1]
        self.body.append(new_body)
    def move(self, position: tuple):
        new_body = self.body[0][0] + position[0], self.body[0][1] + position[1]
        self.body.insert(0, new_body)
        self.body.pop(-1)


class Food(object):
    def __init__(self, location):
        self.location = location


class Game:
    def __init__(self):
        self.board = Board(width=40, height=20)
        self.snake = Snake()

    def render(self):
        [(i, j)] = self.snake.body
        self.board.board[i][j] = self.snake.symbol
        self.board.show()


if __name__ == '__main__':
    b = Board(width=40, height=20)
    b.show()
    s = Snake()
    s.eat((1, 2))
    print(s.body)
    # s.move((1, 3))
    # print(s.body)
    game = Game()
    game.render()
