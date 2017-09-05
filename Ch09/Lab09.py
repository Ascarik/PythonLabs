import random
from tkinter import *


class Lab09:
    def __init__(self):
        window = Tk()
        window.title("Lab09")

        name = ("project", "quizze", "midterm", "final")
        colors = ("red", "blue", "yellow", "green")

        canvas = Canvas(window, width=450, height=400, bg="white")
        canvas.pack()

        list_per = self.generate_list()

        i = 0
        for res in name:
            step = 100 * i

            per = list_per[i] / 100 * 200

            canvas.create_rectangle(50 + step, 300 - per, 100 + step, 300, fill=colors[i])
            canvas.create_text(80 + step, 300 - per - 10, text="{0} -- {1:.1f}%".format(res, list_per[i]))
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
    Lab09()
