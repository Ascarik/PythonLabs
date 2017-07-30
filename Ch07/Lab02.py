class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getStockName(self):
        return self.__name

    def getStockSymbol(self):
        return self.__symbol

    def getPreviousPrice(self):
        return self.__previousClosingPrice

    def setPreviousPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):
        return (self.__previousClosingPrice / self.__currentPrice - 1)


stock = Stock("INTL", "Intel Corparation", 20.5, 20.35)

print("Символ компании:", stock.getStockSymbol())
print("Название компании:", stock.getStockName())
print("Закрытая цена:", stock.getPreviousPrice())
print("Текущая цена:", stock.getCurrentPrice())
print("Измение в %:", round(stock.getChangePercent(), 4))
