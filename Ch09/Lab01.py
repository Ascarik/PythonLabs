from tkinter import *


class Lab01:
    def __init__(self):
        window = Tk()

        window.title("Lab01")

        self.width = 300
        self.height = 300
        self.x = 300 / 2
        self.y = 300 / 2

        self.canvas = Canvas(window, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red", tags="circle")

        frame = Frame(window)
        frame.pack()

        btLeft = Button(frame, text="Left", command=self.__left)
        btRight = Button(frame, text="Right", command=self.__right)
        btUp = Button(frame, text="Up", command=self.__up)
        btDown = Button(frame, text="Down", command=self.__down)

        btLeft.grid(row=1, column=1)
        btRight.grid(row=1, column=2)
        btUp.grid(row=1, column=3)
        btDown.grid(row=1, column=4)

        window.mainloop()

    def __left(self):
        print("left")
        if ((self.x - 5) >= 0):
            self.x -= 5
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red", tags="circle")

    def __right(self):
        print("right")
        if ((self.x + 5) <= self.width):
            self.x += 5
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red", tags="circle")

    def __up(self):
        print("up")
        if ((self.y - 5) >= 0):
            self.y -= 5
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red", tags="circle")

    def __down(self):
        print("down")
        if ((self.y + 5) <= self.height):
            self.y += 5
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red", tags="circle")


if __name__ == '__main__':
    Lab01()
