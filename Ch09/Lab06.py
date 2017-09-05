import random
from tkinter import *


class Lab06:
    def __init__(self):
        window = Tk()
        window.title("Lab06")

        canvas = Canvas(window, width=150, height=150, bg="white")
        canvas.pack()

        xImage = PhotoImage(file="resources/x.gif")
        oImage = PhotoImage(file="resources/o.gif")

        i = 0
        while i < 3:

            j = 0
            stepi = 50 * i

            while j < 3:
                stepj = 50 * j
                if random.randint(0, 1) == 0:
                    image = oImage
                else:
                    image = xImage
                canvas.create_image(25 + stepi, 25 + stepj, image=image)
                j += 1

            i += 1

        window.mainloop()


if __name__ == '__main__':
    Lab06()
