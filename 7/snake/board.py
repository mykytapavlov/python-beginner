class Board:
    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.border = border
        self.board = self.init_board()

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        return ((p2_i - p1_i)**2 + (p2_j - p1_j)**2)**0.5

    def init_board(self):
        board = []
        border_row = [self.border] * self.width
        # add first row
        board.append(border_row)
        # add second to penultimate row
        for i in range(1, self.height - 1):
            # first symbol in row: border
            row = [self.border]
            # second to penultimate symbol in row: space
            for j in range(1, self.width - 1):
                row.append(' ')
            # last symbol in row: border
            row.append(self.border)
            # add row to board
            board.append(row)
        # add last row
        board.append(border_row)
        return board

    def show(self):
        for row in self.board:
            print(' '.join(row))
