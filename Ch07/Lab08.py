import time


class StopWatch:
    def __init__(self):
        self.__startTime = time.time()
        self.__stopTime = 0

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__stopTime = time.time()

    def getElapsedTime(self):
        return self.__stopTime - self.__startTime


watch = StopWatch()

for i in range(1000000):
    print(i)

watch.stop()

print("the execution time ", watch.getElapsedTime())
