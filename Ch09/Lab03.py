from tkinter import *


class Lab03:
    def __init__(self):
        window = Tk()
        window.title("Lab03")

        self.canvas = Canvas(window, width=300, height=300, bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        self.v1 = IntVar()
        rectangle = Radiobutton(frame, text="Rectangle", variable=self.v1, value=1, command=self.processRadiobutton)
        oval = Radiobutton(frame, text="Oval", variable=self.v1, value=2, command=self.processRadiobutton)

        self.v2 = IntVar()
        cbtFill = Checkbutton(frame, text="Filled", variable=self.v2, command=self.processCheckbutton)

        rectangle.grid(row=1, column=1)
        oval.grid(row=1, column=2)
        cbtFill.grid(row=1, column=3)

        self.color = ""
        self.checked = False

        window.mainloop()

    def processRadiobutton(self):
        self.drawFigures()

    def processCheckbutton(self):
        self.drawFigures()

    def drawFigures(self):
        self.color = "red" if self.v2.get() == 1 else ""

        if self.v1.get() != 1:
            self.canvas.delete("circle", "rectangle")
            self.canvas.create_oval(30, 40, 280, 220, fill=self.color, tags="circle")
        else:
            self.canvas.delete("circle", "rectangle")
            self.canvas.create_rectangle(20, 80, 280, 220, fill=self.color, tags="rectangle")


if __name__ == '__main__':
    Lab03()
