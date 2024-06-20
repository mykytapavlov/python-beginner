from time import sleep
from board import Board
from snake import Snake
from apple import Apple
import random


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def init_apple(self):
        available = self.board.available_positions()  # create a set with all available spaces
        available -= set(self.snake.body) | set(self.apple.position)  # filter out snake and last apple position
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
                available = self.board.available_positions()
                possible_moves = self.snake.choices()
                possible_moves &= available  # filter positions inside board from possible snake moves
                if possible_moves:  # get best move
                    min_distance = (self.height**2 + self.width**2)**0.5
                    next_move = None
                    for move in possible_moves:
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
        self.board[i][j] = self.apple.symbol
        # set snake tail
        tail_i, tail_j = self.snake.body[0]
        self.board[tail_i][tail_j] = self.snake.symbols['tail']
        # set snake body
        for body_element in self.snake.body[1:-1]:
            body_i, body_j = body_element
            self.board[body_i][body_j] = self.snake.symbols['body']
        # set snake head
        head_i, head_j = self.snake.body[-1]
        self.board[head_i][head_j] = self.snake.symbols['head']
        # print board
        self.board.show()
        # sleep
        sleep(1)
