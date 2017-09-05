from tkinter import *


class Lab02:
    def __init__(self):
        window = Tk()
        window.title("Lab02")

        label1 = Label(window, text="Investment Amount")
        self.iamount = DoubleVar()
        investmentAmount = Entry(window, textvariable=self.iamount, justify=RIGHT)

        label2 = Label(window, text="Years")
        self.years = IntVar()
        investyears = Entry(window, textvariable=self.years, justify=RIGHT)

        label3 = Label(window, text="Investment Amount")
        self.annualInterestRate = DoubleVar()
        investAnnualInterestRate = Entry(window, textvariable=self.annualInterestRate, justify=RIGHT)

        label4 = Label(window, text="Future Value")
        self.futureValue = DoubleVar()
        investAmount = Label(window, textvariable=self.futureValue, justify=RIGHT)

        button = Button(window, text="Calculate", command=self.calculate).grid(row=5, column=2, sticky=W)

        label1.grid(row=1, column=1, sticky=W)
        investmentAmount.grid(row=1, column=2, sticky=E)
        label2.grid(row=2, column=1, sticky=W)
        investyears.grid(row=2, column=2, sticky=E)
        label3.grid(row=3, column=1, sticky=W)
        investAnnualInterestRate.grid(row=3, column=2, sticky=E)
        label4.grid(row=4, column=1, sticky=W)
        investAmount.grid(row=4, column=2, sticky=E)

        window.mainloop()

    def calculate(self):
        print(self.iamount.get())
        print(self.annualInterestRate.get())
        print(self.years.get())
        futureValue = self.iamount.get() * (1 + self.annualInterestRate.get() / 100 / 12) ** (self.years.get() * 12)
        print(futureValue)
        self.futureValue.set(format(futureValue, ".2f"))


if __name__ == '__main__':
    Lab02()
