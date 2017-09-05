from tkinter import *


class Lab08:
    def __init__(self):
        window = Tk()
        window.title("Lab08")

        canvas = Canvas(window, width=400, height=400, bg="white")
        canvas.pack()

        i = 1
        while i <= 11:
            stepi = 30 * i

            j = 1
            while j <= 12 - i:
                stepj = 30 * j
                canvas.create_text(15 * i + stepj, 375 - stepi, text=str(j))
                j += 1

            i += 1
        window.mainloop()


if __name__ == '__main__':
    Lab08()
