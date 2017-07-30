import datetime


class Time:
    def __init__(self):
        currentTime = datetime.datetime.now()

        self.__hours = currentTime.hour
        self.__minutes = currentTime.minute
        self.__seconds = currentTime.second

        print("Constructor: ", self.__hours, ":", self.__minutes, ":", self.__seconds)

    def getHour(self):
        return self.__hours

    def getMinutes(self):
        return self.__minutes

    def getSeconds(self):
        return self.__seconds

    def setHour(self, hours):
        self.__hours = hours

    def setMinutes(self, minutes):
        self.__minutes = minutes

    def setSeconds(self, seconds):
        self.__seconds = seconds

    def setTime(self, elapseTime):
        seconds = elapseTime % 60
        elapseTime //= 60
        minutes = elapseTime % 60
        elapseTime %= 24
        hours = elapseTime

        self.__hours += hours
        self.__minutes += minutes
        self.__seconds += seconds

        if self.__seconds >= 60:
            self.__minutes += 1
            self.__seconds %= 60

        if self.__minutes >= 60:
            self.__hours += 1
            self.__minutes %= 60

        if self.__hours >= 24:
            self.__hours %= 24

        print(self.__hours, ":", self.__minutes, ":", self.__seconds)


t = Time()
t.setTime(555550)
