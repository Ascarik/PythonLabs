from tkinter import *


class Lab19:
    def __init__(self):
        window = Tk()
        window.title("Lab19")

        self.canvas = Canvas(window, width=400, height=400)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.draw_circle)
        self.canvas.focus_set()

        window.mainloop()

    def draw_circle(self, event):
        x = event.x
        y = event.y
        self.canvas.delete("pointer")
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="green", tags="pointer")


if __name__ == '__main__':
    Lab19()
