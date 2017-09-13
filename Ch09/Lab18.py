from tkinter import *


class Lab18:
    def __init__(self):
        window = Tk()
        window.title("Lab18")

        canvas = Canvas(window, width=400, height=400)
        canvas.pack()

        flag = False
        while True:

            canvas.after(300)
            canvas.update()
            if flag:
                canvas.delete("txt")
                flag = False
            else:
                canvas.create_text(200, 200, text="Welcome", tags="txt")
                flag = True

        window.mainloop()


if __name__ == '__main__':
    Lab18()
