from tkinter import *


class Lab04:
    def __init__(self):
        window = Tk()
        window.title("Lab04")

        canvas = Canvas(window, width=400, height=300, bg="white")
        canvas.pack()

        i = 1
        while i < 31:
            step = 5 * i
            canvas.create_rectangle(0 + step, 0 + step, 400 - step, 300 - step)
            i += 1

        window.mainloop()


if __name__ == '__main__':
    Lab04()
