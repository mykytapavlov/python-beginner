from time import sleep
from board import Board
from snake import Snake
from apple import Apple
import random


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def init_apple(self):
        # save last position
        last_position = self.apple.position
        # create a set with all available spaces
        available = set()
        for i in range(1, self.board.height - 1):
            for j in range(1, self.board.width - 1):
                available.add((i,j))
        available = available.difference(set(self.snake.body)).difference(set(last_position))
        if available:
            # if set of available space is not empty: select random element form it
            self.apple = Apple(position=(random.choice(list(available))))
        else:
            raise GameOverError('No places for apple!')

    def play(self):
        self.apple = Apple(position=(1, 2))
        self.snake.eat(self.apple)
        self.render()

        self.apple = Apple(position=(2, 2))
        self.snake.eat(self.apple)
        self.render()

        self.apple = Apple(position=(2, 3))
        self.snake.eat(self.apple)
        self.render()

        self.snake.move(position=(2,4))
        self.render()

        self.init_apple()
        self.render()

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
        for body_element in self.snake.body[1:-1]:
            body_i, body_j = body_element
            self.board.board[body_i][body_j] = self.snake.symbols['body']
        # set snake head
        head_i, head_j = self.snake.body[-1]
        self.board.board[head_i][head_j] = self.snake.symbols['head']
        # print board
        self.board.show()
        # sleep
        sleep(1)
