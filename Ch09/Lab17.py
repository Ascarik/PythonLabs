from tkinter import *


class Lab17:
    def __init__(self):
        window = Tk()
        window.title("Lab17")

        canvas = Canvas(window, width=900, height=400)
        canvas.pack()

        i = 0
        while True:
            canvas.after(10)
            canvas.update()
            canvas.delete("car")

            canvas.create_polygon(10 + i, 200, 20 + i, 185, 40 + i, 185, 50 + i, 200, 0 + i, 200, fill="yellow",
                                  tags="car")
            canvas.create_rectangle(0 + i, 200, 60 + i, 220, fill="red", tags="car")
            canvas.create_oval(0 + i, 220, 20 + i, 240, fill="black", tags="car")
            canvas.create_oval(40 + i, 220, 60+i, 240, fill="black", tags="car")
            if i == 840:
                i = 0
            else:
                i += 1

        window.mainloop()


if __name__ == '__main__':
    Lab17()
