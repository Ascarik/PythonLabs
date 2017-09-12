from tkinter import *


class Lab13:
    def __init__(self):
        window = Tk()
        window.title("Lab13")

        self.canvas = Canvas(window, width=400, height=250)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.move)

        window.mainloop()

    def move(self, event):
        print("({0}:{1})".format(event.x, event.y))
        self.text(event.x, event.y, "({0}:{1})".format(event.x, event.y))

    def text(self, x, y, text):
        self.canvas.delete("text")
        self.canvas.create_text(x, y-10, text=text, tags="text")


if __name__ == '__main__':
    Lab13()
