from time import sleep
import os
import random
import math


class Board:

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        d = math.sqrt((p2_i-p1_i)**2 + (p2_j-p1_j)**2)
        # d = math.dist(p1, p2)
        return d

    def __init__(self, width, height, top_border="<", bottom_border=">", vert_border="^"):
        self.snake = Snake()
        self.top_boarders = top_border
        self.bottom_boarders = bottom_border
        self.vert_boarders = vert_border
        self.width = width
        self.height = height
        self.board = self.init_board()

    def init_board(self):
        new_board = []
        for i in range(self.height):
            if i == 0:
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
        self.body.pop(0)

    def choices(self):
        next_positions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        result = []
        for next_position in next_positions:
            new_positions = self.body[-1][0] + next_position[0], self.body[-1][1] + next_position[1]
            for new_position in new_positions:
                if new_position in self.body:
                    continue
            result.append(new_positions)
        # print(result)
        # rand_result = result[random.randrange(len(result))]
        # return choices that do not intersect with snake body coords
        return result


class Apple:
    def __init__(self, symbol='$', position=(2, 2)):
        self.position = position
        self.symbol = symbol


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width, height):
        self.symbol = "o"
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def init_apple(self):
        last_pos = self.apple.position
        self.board = Board(self.width, self.height)
        positions = []
        for x in range(self.height):
            for y in range(self.width):
                z = (item for item in self.snake.body)
                if (x, y) != last_pos and (x, y) not in z:
                    if self.board.board[x][y] == ' ':
                        positions.append((x, y))

        if positions:
            position = random.choices(positions)[0]
            self.apple = Apple(position=position, symbol="$")
            return self.apple.position
        else:
            raise GameOverError('No places for apple!')

    def play(self):
        game_cycles = 20
        try:
            self.render()  # initial render of board, snake and apple
            while game_cycles > 0:  # start our game
                snake_i, snake_j = self.snake.body[-1]  # remember last position of snake's head
                move = None
                # TODO: find next possible position (next_move) for snake to move
                possible_moves = self.snake.choices()
                next_moves = []
                for move in possible_moves:
                    # print(next_move, type(next_move))
                    if move[0] != 0 and move[1] != 0:
                        next_moves.append(move)
                # print(next_moves)
                distances = []
                for move in next_moves:
                    dist = self.board.distance(move, self.apple.position)
                    distances.append(dist)
                # print(distances)
                res = {}
                for key in next_moves:
                    for value in distances:
                        res[key] = value
                        distances.remove(value)
                        break
                # print(str(res))
                next_move = min(res, key=res.get)
                # print(next_move)
                self.snake.move(next_move)
                while True:
                    if next_move == self.apple.position:
                        # TODO: eat apple, render this action, init new apple and render it on board
                        self.snake.body.append(next_move)
                        self.snake.eat(next_move)
                        self.init_apple()
                        continue
                    self.snake.move(next_move)
                    self.render()
                    if next_move in self.snake.body:
                        GameOverError('Game over:(')
                        break
                    if next_move is None:  # there is no possible move for snake
                        self.snake.move((snake_i + 1, snake_j + 1))  # just do one move forward for snake
                        self.render()  # render last move
                        GameOverError('No moves for snake!')  # end the game (snake does not have next valid move)
                game_cycles -= 1
        except GameOverError:
            print('Game Over!')

    def clear(self):
        self.board = Board(self.width, self.height)
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def render(self):
        self.clear()
        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol
        for i, j in self.snake.body:
            self.board.board[i][j] = self.snake.symbol
        self.board.show()
        sleep(2)


if __name__ == '__main__':
    game = Game(15, 10)
    game.play()
    # s = Snake(position=(3, 1))
    # print(s.choices())
    # game.init_apple()
    # b = Board(width=40, height=20)
    # b.show()
    # # s.move((1, 3))
    # print(s.body)
    # print(s.head)
    # # s.eat((1, 2))
    # # print(s.body)
