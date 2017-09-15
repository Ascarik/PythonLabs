import math
from tkinter import *


class Lab22:
    def __init__(self):
        window = Tk()
        window.title("Lab22")

        self.canvas = Canvas(window, width=400, height=400, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Key>", self.speed_hand)
        self.canvas.focus_set()
        self.speed = 10

        i = -90
        flag = False
        while True:
            if flag:
                i += 1
            else:
                i -= 1

            self.create_hands(i)

            if i == 0:
                flag = False

            if i == -180:
                flag = True

        window.mainloop()

    def create_hands(self, number):

        self.canvas.after(self.speed)
        self.canvas.update()
        for i in range(2):
            if i == 0:
                self.canvas.delete("pointer")
            else:

                radius = 150
                radian = (number) * (2 * math.pi / 360)

                x = 200 + radius * math.cos(radian)
                y = 200 - radius * math.sin(radian)
                self.canvas.create_line(200, 200, x, y, fill="red", tags="pointer")
                self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red", tags="pointer")

    def speed_hand(self, event):
        print(event.keycode)
        if event.keycode == 111:
            self.speed += 5
        if event.keycode == 116:
            self.speed -= 5


if __name__ == '__main__':
    Lab22()
