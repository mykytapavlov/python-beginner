class Board:
    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.border = border
        self.board = self.init_board()

    def init_board(self):
        board = []
        # first row
        border_row = [self.border] * self.width
        board.append(border_row)
        # second to penultimate row
        for i in range(self.height):
            row = [self.border]
            for j in range(1,self.width-1):
                row.append(' ')
            row.append(self.border)
            board.append(row)
        # last row
        board.append(border_row)
        return board

    def show(self):
        for row in self.board:
            print(' '.join(row))