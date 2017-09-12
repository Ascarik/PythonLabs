from tkinter import *


class Lab14:
    def __init__(self):
        window = Tk()
        window.title("Lab14")
        self.dest = 20
        self.x = 200
        self.y = 125

        self.canvas = Canvas(window, width=400, height=250)
        self.canvas.pack()

        self.canvas.bind("<Key>", self.move)
        self.canvas.focus_set()

        window.mainloop()

    def move(self, event):
        print(event.keycode)
        if event.keycode == 113:
            self.line(self.x - 20, self.y)
        elif event.keycode == 114:
            self.line(self.x + 20, self.y)
        elif event.keycode == 116:
            self.line(self.x, self.y + 20)
        elif event.keycode == 111:
            self.line(self.x, self.y - 20)

    def line(self, x, y):
        self.canvas.create_line(self.x, self.y, x, y, tags="text")
        self.x, self.y = x, y


if __name__ == '__main__':
    Lab14()
