import math

class Board:
    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.border = border
        self.board = self.init_board()

    def init_board(self):
        board = []

        for i in range(self.height):
            if i in {0, self.height - 1}:
                row = [self.border] * self.width
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(self.border)
                    else:
                        row.append(' ')
            board.append(row)
        return board

    def show(self):
        for row in self.board:
            print(' '.join(row))

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        return math.sqrt((p1_i - p2_i) ** 2 + (p1_j - p2_j) ** 2)
