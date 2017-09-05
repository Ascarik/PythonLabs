from tkinter import *


class Lab05:
    def __init__(self):
        window = Tk()
        window.title("Lab05")

        canvas = Canvas(window, width=400, height=400, bg="white")
        canvas.pack()

        self.color = "white"
        i = 0
        while i < 8:

            j = 0
            stepi = 50 * i

            while j < 8:
                stepj = 50 * j
                canvas.create_rectangle(0 + stepi, 0 + stepj, 50 + stepi, 50 + stepj, fill=self.color)
                self.__changeColor()
                j += 1

            self.__changeColor()

            i += 1

        window.mainloop()

    def __changeColor(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"


if __name__ == '__main__':
    Lab05()
