import math
import random
from tkinter import *


class Lab10:
    def __init__(self):
        window = Tk()
        window.title("Lab10")

        name = ("project", "quizze", "midterm", "final")
        colors = ("red", "blue", "purple", "green")

        canvas = Canvas(window, width=400, height=400, bg="white")
        canvas.pack()

        i = 0
        step = 0
        percent = self.generate_list()

        for res in name:
            per = percent[i] / 100
            canvas.create_arc(250, 250, 80, 80, start=step, extent=(360 * per), fill=colors[i])

            radius = 130
            radian = (step + (360 * per / 2)) * (2 * math.pi / 360)

            x = 160 + radius * math.cos(radian)
            y = 160 - radius * math.sin(radian)

            canvas.create_text(x, y, text="{0} -- {1}%".format(name[i], percent[i]), fill=colors[i])
            step += 360 * per
            i += 1

        window.mainloop()

    def generate_list(self):
        percent = list()
        hundred = 100

        while 0 <= len(percent) <= 4:
            per = random.randint(0, 100)

            if hundred - per >= 0:
                percent.append(per)
                hundred -= per

                if len(percent) == 3:
                    percent.append(hundred)
                    break
            if hundred == 0:
                percent.append(0)

        return percent


if __name__ == '__main__':
    Lab10()
