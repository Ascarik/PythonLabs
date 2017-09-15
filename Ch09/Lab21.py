from tkinter import *


class Lab21:
    def __init__(self):
        window = Tk()
        window.title("Lab21")

        self.canvas = Canvas(window, width=400, height=400)
        self.canvas.pack()
        self.x1 = 100
        self.y1 = 100
        self.x2 = 300
        self.y2 = 200

        self.canvas.create_rectangle(100,100,300,200)

        self.canvas.bind("<B1-Motion>", self.draw_circle)
        self.canvas.focus_set()

        window.mainloop()

    def draw_circle(self, event):

        self.canvas.delete("pointer")
        if self.x1<=event.x<=self.x2 and self.y1<=event.y<=self.y2:
            self.canvas.create_text(event.x - 10, event.y - 10, text="Mouse pointer is in the circle", fill="green", tags="pointer")
        else:
            self.canvas.create_text(event.x - 10, event.y - 10, text="Mouse pointer is not in the circle", fill="red",  tags="pointer")


if __name__ == '__main__':
    Lab21()
