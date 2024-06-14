from board import Board
from snake import Snake
from apple import Apple


class Game:
    def __init__(self):
        self.board = Board(width=15, height=15)
        self.snake = Snake()
        self.apple = Apple()

    def render(self):
        i, j = self.snake.position
        self.board.board[i][j] = self.snake.body
        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol
        self.board.show()