import tkinter
from Fifteen.controller.controller import Controller


class View:
    def __init__(self):
        self.SQUARE_SIZE = 100
        self.control = Controller()
        self.root = tkinter.Tk()
        self.root.title("Пятнашки")
        self.c = tkinter.Canvas(self.root,
                                width=self.SQUARE_SIZE * self.control.get_board_size(),
                                height=self.SQUARE_SIZE * self.control.get_board_size(),
                                bg='#808080')
        self.c.bind('<Button-1>', self.click)
        self.c.pack()

    def click(self, event):
        x, y = event.x, event.y
        x = x // self.SQUARE_SIZE + 1
        y = y // self.SQUARE_SIZE + 1
        self.control.move_field(y, x)
        self.draw_board()
        if self.control.check_victory():
            self.show_victory()

    def show_victory(self):
        self.c.create_rectangle(self.SQUARE_SIZE / 5,
                                self.SQUARE_SIZE * self.control.get_board_size()/2 - 10*self.control.get_board_size(),
                                self.control.get_board_size() * self.SQUARE_SIZE - self.SQUARE_SIZE/5,
                                self.SQUARE_SIZE * self.control.get_board_size()/2 + 10*self.control.get_board_size(),
                                fill='#000000',
                                outline='#FFFFFF')
        self.c.create_text(self.SQUARE_SIZE * self.control.get_board_size()/2,
                           self.SQUARE_SIZE * self.control.get_board_size()/1.9,
                           text="Победа",
                           font="Helvetica {} bold".format(int(10 * self.control.get_board_size())),
                           fill='#00FF00')

    def draw_board(self):
        self.c.delete('all')
        for i in range(self.control.get_board_size()):
            for j in range(self.control.get_board_size()):
                index = str(self.control.get_number(i + 1, j + 1))
                if index != '0':
                    self.c.create_rectangle(j * self.SQUARE_SIZE, i * self.SQUARE_SIZE,
                                            j * self.SQUARE_SIZE + self.SQUARE_SIZE,
                                            i * self.SQUARE_SIZE + self.SQUARE_SIZE,
                                            fill='#43ABC9',
                                            outline='#FFFFFF')
                    self.c.create_text(j * self.SQUARE_SIZE + self.SQUARE_SIZE/2,
                                       i * self.SQUARE_SIZE + self.SQUARE_SIZE/2,
                                       text=index,
                                       font="Arial {} italic".format(int(self.SQUARE_SIZE/4)),
                                       fill='#FFFFFF')

    def run(self):
        self.draw_board()
        self.root.mainloop()
