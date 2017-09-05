from tkinter import *


class Lab07:
    def __init__(self):
        window = Tk()
        window.title("Lab07")

        canvas = Canvas(window, width=400, height=400, bg="white")
        canvas.pack()

        i = 1
        while i < 8:
            step = 50 * i
            # canvas.create_rectangle(0 + stepi, 0 + stepj, 50 + stepi, 50 + stepj, fill=self.color)
            canvas.create_line(0 + step, 0, 0 + step, 400)
            canvas.create_line(0, 0 + step, 400, 0 + step)
            i += 1

        window.mainloop()


if __name__ == '__main__':
    Lab07()
