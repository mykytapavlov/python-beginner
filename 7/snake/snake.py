import random
from time import sleep


class Board:
    def __init__(self, width, height, boarder='*'):
        self.width = width
        self.height = height
        self.boarder = boarder
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
            print(''.join(row))

    def __getitem__(self, index):
        return self.board[index]

    def place_a_snake(self, current_snake: list):
        counter = 0
        for x, y in current_snake:
            if counter == 0:
                self.board[x][y] = '1'
                counter += 1
            elif counter == len(current_snake) - 1:
                self.board[x][y] = 'e'
            else:
                self.board[x][y] = 'o'
                counter += 1
        # try to use range here for current_snake and then for loop

    def choices(self, snake_body):
        a, b = snake_body[0]
        print(a, b)
        positions_around = [
            (a - 1, b),
            (a + 1, b),
            (a, b - 1),
            (a, b + 1)
        ]
        available_positions = []

        for i in range(0, len(positions_around)):
            if self.board[positions_around[i][0]][positions_around[i][1]] == ' ':
                available_positions.append(positions_around[i])
        print(f'av = {available_positions}')

    def place_an_apple(self, last_position, symbol='@'):
        list_of_empty_positions = []
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if self.board[i][j] == ' ' and self.board[i][j] != last_position:
                    list_of_empty_positions.append((i, j))

        if list_of_empty_positions:
            x, y = random.choice(list_of_empty_positions)
            self.board[x][y] = symbol
            apple_position = (x, y)
            return apple_position
        else:
            raise Exception("Game over! No places for apple")


class Snake:
    def __init__(self, symbol='o', position=(1, 1)):
        self.symbol = symbol
        self.body = [position]

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        self.body.insert(0, position)
        self.body.pop()


class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def play(self):
        apple = (1, 2)
        self.snake.eat(apple)
        self.render()
        sleep(2)

        apple = (2, 2)
        self.snake.eat(apple)
        self.render()
        sleep(2)

        apple = (2, 3)
        self.snake.eat(apple)
        self.render()
        sleep(2)
        self.init_apple()
        # apple_position = self.board.place_an_apple()
        # print(f'apple position= {apple_position}')
        self.board.show()

    def clear(self):
        self.board.board = self.board.init_board()

    def render(self):
        self.clear()
        # self.play()
        self.board.place_a_snake(self.snake.body)
        # TODO: place snake body on the board
        self.board.show()
        self.board.choices(self.snake.body)

    def init_apple(self):
        last_position = self.apple.position
        self.apple.position = self.board.place_an_apple(last_position)


class Apple:
    def __init__(self, symbol='$', position=(2, 2)):
        self.position = position
        self.symbol = symbol


if __name__ == '__main__':
    game = Game()
    game.play()

