from tkinter import *


class Lab20:
    def __init__(self):
        window = Tk()
        window.title("Lab20")

        self.canvas = Canvas(window, width=400, height=400)
        self.canvas.pack()
        self.x = 200
        self.y = 200
        self.radius = 100

        self.canvas.create_oval(100,100,300,300)

        self.canvas.bind("<B1-Motion>", self.draw_circle)
        self.canvas.focus_set()

        window.mainloop()

    def draw_circle(self, event):
        x = (event.x - self.x)**2
        y = (event.y- self.y)**2
        d = (x+y)**0.5
        self.canvas.delete("pointer")
        if d<=self.radius:
            self.canvas.create_text(event.x - 10, event.y - 10, text="Mouse pointer is in the circle", fill="green", tags="pointer")
        else:
            self.canvas.create_text(event.x - 10, event.y - 10, text="Mouse pointer is not in the circle", fill="red",  tags="pointer")


if __name__ == '__main__':
    Lab20()
