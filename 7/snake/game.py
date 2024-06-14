from board import Board
from snake import Snake
from apple import Apple


class Game:
    def __init__(self):
        self.board = Board(width=20, height=20)
        self.snake = Snake()
        self.apple = Apple()

    def render(self):
        apple = Apple(position=(1, 2))
        self.snake.eat(apple)

        apple = Apple(position=(2, 2))
        self.snake.eat(apple)

        apple = Apple(position=(2, 3))
        self.snake.eat(apple)

        # set apple
        apple = Apple(position=(3,4))
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

        self.board.show()
