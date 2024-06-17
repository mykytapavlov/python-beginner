class Color:
    """
    ANSI Colors for terminal
    """
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
            print(' '.join([self.colored(symbol) for symbol in row]))
