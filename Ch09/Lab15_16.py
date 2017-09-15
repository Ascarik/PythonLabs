from tkinter import *


class Lab15_16:
    def __init__(self):
        window = Tk()
        window.title("Lab15_16")

        canvas = Canvas(window, width=400, height=400)
        canvas.pack()

        step = 0
        degr = 45
        width = 80
        height = 80
        center_x = 330
        center_y = 330
        i = 0
        while True:
            canvas.after(100)
            canvas.update()
            canvas.delete("fan")
            step += i
            canvas.create_arc(center_x, center_y, width, height, start=step, extent=degr, fill="blue", tags="fan")
            step += 90
            canvas.create_arc(center_x, center_y, width, height, start=step, extent=degr, fill="blue", tags="fan")
            step += 90
            canvas.create_arc(center_x, center_y, width, height, start=step, extent=degr, fill="blue", tags="fan")
            step += 90
            canvas.create_arc(center_x, center_y, width, height, start=step, extent=degr, fill="blue", tags="fan")
            if i == 360:
                i = -1
            else:
                i += 1

        window.mainloop()


if __name__ == '__main__':
    Lab15_16()
