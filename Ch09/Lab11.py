import datetime
import math
from tkinter import *


class Lab11:
    def __init__(self):
        window = Tk()
        window.title("Lab11")

        self.canvas = Canvas(window, width=400, height=400, bg="white")
        self.canvas.pack()

        self.canvas.create_oval(50, 50, 350, 350)
        time = datetime.datetime.now()
        hour = int(time.hour)
        minutes = int(time.minute)
        seconds = int(time.second)
        self.create_watch()
        self.create_hands(hour, minutes, seconds)
        print(hour, minutes, seconds)

        window.mainloop()

    def create_hands(self, hour: int, minutes: int, seconds: int):
        hour -= 3
        radius = 90
        radian = hour * (-30) * (2 * math.pi / 360)

        x = 200 + radius * math.cos(radian)
        y = 200 - radius * math.sin(radian)
        self.canvas.create_line(200, 200, x, y, fill="green")

        minutes -= 15
        radius = 120
        radian = minutes * (-6) * (2 * math.pi / 360)

        x = 200 + radius * math.cos(radian)
        y = 200 - radius * math.sin(radian)
        self.canvas.create_line(200, 200, x, y, fill="blue")

        seconds -= 15
        radius = 150
        radian = seconds * (-6) * (2 * math.pi / 360)

        x = 200 + radius * math.cos(radian)
        y = 200 - radius * math.sin(radian)
        self.canvas.create_line(200, 200, x, y, fill="red")

        self.canvas.create_text(195, 380, text="{0}:{1}:{2}".format(hour + 3, minutes + 15, seconds + 15))

    def create_watch(self):
        radius = 140
        step = 60
        for i in range(1, 13, 1):
            radian = step * (2 * math.pi / 360)

            x = 200 + radius * math.cos(radian)
            y = 200 - radius * math.sin(radian)
            step -= 30
            self.canvas.create_text(x, y, text=str(i))


if __name__ == '__main__':
    Lab11()
