from time import sleep
import os


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
    def __init__(self, symbol="o", position=(1, 1)):
        self.symbol = symbol
        self.body = [position]

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        self.body.append(position)
        self.body.pop(-1)


class Apple(object):
    def __init__(self, location):
        self.location = location


class Game:
    def __init__(self, width=40, height=20):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()

    def play(self):
        self.clear()
        apple = (1, 2)
        self.snake.eat(apple)
        apple = Apple(location=apple)
        i, j = apple.location
        self.board.board[i][j] = self.snake.symbol
        self.render()
        sleep(2)

        self.clear()
        apple = (2, 2)
        self.snake.eat(apple)
        apple = Apple(location=apple)
        i, j = apple.location
        self.board.board[i][j] = self.snake.symbol
        self.render()
        sleep(2)

        self.clear()
        apple = (2, 3)
        self.snake.eat(apple)
        apple = Apple(location=apple)
        i, j = apple.location
        self.board.board[i][j] = self.snake.symbol
        self.render()
        sleep(2)
        self.clear()

    def clear(self):
        os.system('cls')

    def render(self):
        i, j = self.snake.body[0]
        self.board.board[i][j] = self.snake.symbol
        i, j = self.snake.body[1]
        self.board.board[i][j] = self.snake.symbol
        self.board.show()


if __name__ == '__main__':
    game = Game()
    game.play()
    # # b = Board(width=40, height=20)
    # # b.show()
    # s = Snake()
    # # s.move((1, 3))
    # print(s.body)
    # print(s.head)
    # # s.eat((1, 2))
    # # print(s.body)
