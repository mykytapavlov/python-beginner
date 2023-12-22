from time import sleep
import random


class Color:
    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE: str = '\033[4m'
    PINK: str = '\033[38;5;206m'


class Board:
    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        return abs(p1_i - p2_i) + abs(p1_j - p2_j)

    @staticmethod
    def colored(symbol: str) -> str:
        if symbol == '*':
            return f'{Color.WARNING}{symbol}{Color.ENDC}'
        elif symbol == '@':
            return f'{Color.FAIL}{symbol}{Color.ENDC}'
        elif symbol == 'o':
            return f'{Color.OKGREEN}{symbol}{Color.ENDC}'
        elif symbol == '%':
            return f'{Color.PINK}{symbol}{Color.ENDC}'
        elif symbol == '^':
            return f'{Color.PINK}{symbol}{Color.ENDC}'
        else:
            return symbol

    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.boarder = border
        self.board = self.init_board()

    def init_board(self):
        board = []

        for i in range(self.height):
            if i in {0, self.height - 1}:
                row = [self.boarder] * self.width
                board.append(row)
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(self.boarder)
                    else:
                        row.append(' ')
                board.append(row)
        return board

    def show(self):
        for row in self.board:
            row_str = ' '.join([self.colored(cell) for cell in row])
            print(row_str)


class GameOverError(Exception):
    pass


class Apple:
    def __init__(self, symbol='$', position=(2, 2)):
        self.position = position
        self.symbol = symbol


class Snake:
    def __init__(self, body_symbol='o', tail_symbol='^', head_symbol='%', position=(1, 1)):
        self.body_symbol = body_symbol
        self.tail_symbol = tail_symbol
        self.head_symbol = head_symbol
        self.body = [position]

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        self.body.append(position)
        self.body.pop(0)

    def choices(self):
        possible_moves = set()
        i, j = self.body[-1]

        # Adding possible moves (up, down, left, right)
        possible_moves.add((i - 1, j))
        possible_moves.add((i + 1, j))
        possible_moves.add((i, j - 1))
        possible_moves.add((i, j + 1))

        # Filter out moves that overlap with snake body
        possible_moves -= set(self.body)

        return possible_moves


class Game:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def clear(self):
        self.board = Board(self.width, self.height)

    def init_apple(self):
        last_position = self.apple.position

        # Finding a new place for the apple
        while True:
            new_i = random.randint(1, self.height - 2)
            new_j = random.randint(1, self.width - 2)
            if (new_i, new_j) in self.snake.body:
                continue
            elif (new_i, new_j) == last_position:
                continue
            else:
                break

        self.apple = Apple(position=(new_i, new_j))

    def render(self):
        self.clear()

        for idx, position in enumerate(self.snake.body):
            i, j = position
            if idx == len(self.snake.body) - 1:
                # Head of the snake
                self.board.board[i][j] = self.snake.head_symbol
            elif idx == 0:
                # Tail of the snake
                self.board.board[i][j] = self.snake.tail_symbol
            else:
                # Body of the snake
                self.board.board[i][j] = self.snake.body_symbol

        # Place apple on the board
        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol

        self.board.show()
        sleep(2)

    def play(self):
        try:
            while True:
                self.render()
                sleep(2)
                snake_i, snake_j = self.snake.body[-1]
                next_moves = self.snake.choices()

                if not next_moves:
                    self.snake.move((snake_i + 1, snake_j + 1))
                    raise GameOverError('No moves for snake!')

                min_distance = None
                best_move = None

                for move in next_moves:
                    if move is not None:
                        distance = Board.distance(move, self.apple.position)
                        if min_distance is None or distance < min_distance:
                            min_distance = distance
                            best_move = move

                if best_move is None:
                    raise GameOverError('No valid moves for snake!')

                if best_move == self.apple.position:
                    self.snake.eat(best_move)
                    self.init_apple()
                else:
                    self.snake.move(best_move)
        except GameOverError:
            print('Game Over!')

if __name__ == '__main__':
    game = Game()
    game.play()
