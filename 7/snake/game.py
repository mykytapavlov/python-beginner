from time import sleep
from board import Board
from snake import Snake
from apple import Apple
import random


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width=6, height=6):
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
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                available.add((i,j))
        available -= set(self.snake.body) | set(last_position)
        try:
            # if set of available space is not empty: select random element from it
            self.apple = Apple(position=(random.choice(list(available))))
        except IndexError:
            raise GameOverError('No places for apple!')

    def play(self):
        try:
            self.render()  # initial render of board, snake and apple
            while True:  # start our game
                snake_i, snake_j = self.snake.body[-1]  # remember last position of snake's head
                border_positions = set()  # create a set with all border positions
                for j in range(0, self.width):  # add positions of the border for the first and last rows
                    border_positions.add((0, j))
                    border_positions.add((self.height - 1, j))
                for i in range(1, self.height - 1):  # add positions of the border for the intermediate rows
                    border_positions.add((i, 0))
                    border_positions.add((i, self.width - 1))
                available_moves = self.snake.choices()
                available_moves -= border_positions  # filter out border positions from possible snake moves
                if available_moves:  # get best move
                    min_distance = (self.height**2 + self.width**2)**0.5
                    next_move = None
                    for move in available_moves:
                        current_distance = self.board.distance(self.apple.position, move)
                        if current_distance < min_distance:
                            min_distance = current_distance
                            next_move = move
                else:  # there is no possible move for snake
                    self.snake.move((snake_i, snake_j + 1))  # just do one move forward for snake
                    self.render()  # render last move
                    raise GameOverError('No moves for snake!')  # end the game (snake does not have next valid move)
                if next_move == self.apple.position:
                    self.snake.eat(self.apple)  # eat apple
                    self.render()  # render this action
                    self.init_apple()  # init new apple
                    self.render()  # render it on board
                    continue  # go to next game cycle
                # if game is not over, and snake did not eat the apple in current game cycle,
                # then it means it can simply move on next valid position:
                self.snake.move(next_move)
                self.render()
        except GameOverError as e:
            print(f'Game Over! {e}')

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
