


class PlayingField:
    def __init__(self):
        self.BOARD_SIZE = 4
        self.EMPTY_POSITION = (self.BOARD_SIZE, self.BOARD_SIZE)
        self.cur_empty_field = self.EMPTY_POSITION
        self.fields = {}

    def init_fields(self, numbers):
        index = 0
        for i in range(1, self.BOARD_SIZE + 1):
            for j in range(1, self.BOARD_SIZE + 1):
                if i == self.EMPTY_POSITION[0] and j == self.EMPTY_POSITION[1]:
                    self.fields[(i, j)] = 0
                else:
                    self.fields[(i, j)] = numbers[index]
                    index += 1

    def get_board_size(self):
        return self.BOARD_SIZE

    def get_empty_position(self):
        return self.cur_empty_field

    def set_empty_position(self, row, col):
        self.cur_empty_field = (row, col)

    def get_field(self, row, col):
        if 0 < row <= self.BOARD_SIZE and 0 < col <= self.BOARD_SIZE:
            return self.fields[(row, col)]

    def set_field(self, row, col, value):
        if 0 < row <= self.BOARD_SIZE and 0 < col <= self.BOARD_SIZE:
            self.fields[(row, col)] = value

    def is_consist(self):
        number = 1
        for i in range(1, self.BOARD_SIZE + 1):
            for j in range(1, self.BOARD_SIZE + 1):
                if self.fields[(i, j)] != number:
                    return False
                else:
                    number += 1
        return True
