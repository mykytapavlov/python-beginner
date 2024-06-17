from time import sleep
from board import Board
from snake import Snake
from apple import Apple


class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def play(self):
        self.apple = Apple(position=(1, 2))
        self.snake.eat(self.apple)
        self.render()
        print(self.snake.choices())
        sleep(2)

        self.apple = Apple(position=(2, 2))
        self.snake.eat(self.apple)
        self.render()
        print(self.snake.choices())
        sleep(2)

        self.apple = Apple(position=(2, 3))
        self.snake.eat(self.apple)
        self.render()
        print(self.snake.choices())
        sleep(2)

        self.snake.move(position=(2,4))
        self.render()
        print(self.snake.choices())
        sleep(2)

        self.apple = Apple(position=(3, 4))
        self.render()
        print(self.snake.choices())
        sleep(2)

    def clear(self):
        # clear console output
        print("\033[H\033[J", end="")
        # clear board
        self.board = Board(self.width, self.height)

    def render(self):
        self.clear()
        # set apple
        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol
        # set snake tail
        tail_i, tail_j = self.snake.body[0]
        self.board.board[tail_i][tail_j] = self.snake.symbols['tail']
        # set snake body
        for body_index in range(1,len(self.snake.body)-1):
            body_i, body_j = self.snake.body[body_index]
            self.board.board[body_i][body_j] = self.snake.symbols['body']
        # set snake head
        head_i, head_j = self.snake.body[-1]
        self.board.board[head_i][head_j] = self.snake.symbols['head']
        # print board
        self.board.show()
