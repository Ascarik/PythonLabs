from tkinter import *


class Lab12:
    def __init__(self):
        window = Tk()
        window.title("Lab12")

        self.canvas = Canvas(window, width=400, height=250)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.pressLeft)
        self.canvas.bind("<Button-3>", self.pressRight)

        window.mainloop()

    def pressLeft(self, event):
        self.text("Programming is fun")

    def pressRight(self, event):
        self.text("It is fun to program")

    def text(self, text):
        self.canvas.delete("text")
        self.canvas.create_text(200, 125, text=text, tags="text")


if __name__ == '__main__':
    Lab12()
