from Fifteen.model.playField import PlayingField
from random import shuffle


class Controller:
    def __init__(self):
        self.field = PlayingField()
        self.field.init_fields(self.build_numbers_mas())

    def build_numbers_mas(self):
        numbers = []
        for number in range(1, self.field.get_board_size() ** 2):
            numbers.append(number)
        shuffle(numbers)
        return numbers

    def get_board_size(self):
        return self.field.get_board_size()

    def get_number(self, row, col):
        return self.field.get_field(row, col)

    def get_empty(self):
        return self.field.get_empty_position()

    def move_field(self,  row, col):
        num = self.field.get_field(row, col)
        empty = self.field.get_empty_position()
        if self.is_empty_neighbor(row, col):
            self.field.set_field(row, col, 0)
            self.field.set_field(empty[0], empty[1], num)
            self.field.set_empty_position(row, col)

    def is_empty_neighbor(self, row, col):
        if self.get_empty()[0] == row + 1 or self.get_empty()[0] == row - 1:
            if self.get_empty()[1] == col:
                return True
        elif self.get_empty()[0] == row:
            if self.get_empty()[1] == col + 1 or self.get_empty()[1] == col - 1:
                return True
        return False

    def check_victory(self):
        return self.field.is_consist()

