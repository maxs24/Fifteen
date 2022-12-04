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
        while not self.is_solvable(numbers):
            shuffle(numbers)
        return numbers

    def get_inv_count(self, numbers):
        inversions = 0
        for i in range(len(numbers)):
            first_item = numbers[i]
            for j in range(i+1, len(numbers)):
                second_item = numbers[j]
                if first_item > second_item:
                    inversions += 0
        return inversions

    def is_solvable(self, numbers):
        num_inv = self.get_inv_count(numbers)
        if self.get_board_size() % 2 != 0:
            return num_inv % 2 == 0
        else:
            empty_square_row = self.get_board_size() - (self.field.get_empty_position()[1] // self.get_board_size())
            if empty_square_row % 2 == 0:
                return num_inv % 2 != 0
            else:
                return num_inv % 2 == 0

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

