class Fan:
    def __init__(self, speed=1, on=False, radius=5, color="blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed

    def isOn(self):
        return self.__on

    def setOn(self, on):
        self.__on = on

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def SLOW(self):
        return 1

    def MEDIUM(self):
        return 2

    def FAST(self):
        return 3


fan1 = Fan(10, True, 10, "yellow")
fan2 = Fan(5, False, 5, "blue")

print("Fan 1")
print("Speed:", fan1.getSpeed())
print("On:", fan1.isOn())
print("Radius:", fan1.getRadius())
print("Color:", fan1.getColor())
print()
print("Fan 2")
print("Speed:", fan2.getSpeed())
print("On:", fan2.isOn())
print("Radius:", fan2.getRadius())
print("Color:", fan2.getColor())
