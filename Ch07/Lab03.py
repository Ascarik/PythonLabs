class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12 / 100

    def getMonthlyInterest(self):
        return self.getMonthlyInterestRate() * self.__balance

    def getWithdraw(self):
        self.__balance -= 2500

    def getDeposit(self):
        self.__balance += 3000


account = Account(1122, 20000, 4.5)

print("Balance =", account.getBalance())
print("Balance ID =", account.getId())

print("The monthly interest =", account.getMonthlyInterest())
print("The monthly interest rate =", account.getMonthlyInterestRate())
account.getWithdraw()
print("Balance =", account.getBalance())
