import random
from time import sleep
from board import Board
from snake import Snake
from apple import Apple


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = Board(width, height)
        self.snake = Snake()
        self.apple = Apple()

    def play(self):
        try:
            self.render()

            while True:
                snake_i, snake_j = self.snake.body[-1]

                # Check if snake hits the board walls
                if snake_i == 0 or snake_i == self.height - 1 or snake_j == 0 or snake_j == self.width - 1:
                    raise GameOverError('Snake hit the board wall!')

                possible_moves = self.snake.choices()

                if not possible_moves:
                    self.render()
                    raise GameOverError('No moves for snake!')

                min_distance = float('inf')
                best_move = None

                for move in possible_moves:
                    dist = Board.distance(move, self.apple.position)
                    if dist < min_distance:
                        min_distance = dist
                        best_move = move

                if best_move == self.apple.position:
                    self.snake.eat(best_move)
                    self.init_apple()
                    self.render()
                else:
                    self.snake.move(best_move)
                    self.render()

                sleep(0.5)

        except GameOverError as e:
            print(f'Game Over! {e}')

    def render(self):
        self.clear()
        head_i, head_j = self.snake.body[-1]
        tail_i, tail_j = self.snake.body[0]
        self.board.board[head_i][head_j] = self.snake.head_symbol
        self.board.board[tail_i][tail_j] = self.snake.symbol

        for segment in self.snake.body[1:-1]:  # Render body segments
            segment_i, segment_j = segment
            self.board.board[segment_i][segment_j] = self.snake.symbol

        apple_i, apple_j = self.apple.position
        self.board.board[apple_i][apple_j] = self.apple.symbol

        self.board.show()

    def clear(self):
        self.board = Board(self.width, self.height)

    def init_apple(self):
        snake_positions = set(self.snake.body)

        # Try to place apple within the playable area of the board
        for _ in range(self.width * self.height):
            new_position = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))

            if new_position not in snake_positions:
                self.apple = Apple(position=new_position)
                return

        raise GameOverError('No places for apple!')


if __name__ == '__main__':
    game = Game(width=10, height=10)
    game.play()
