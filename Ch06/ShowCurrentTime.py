import time


def getCurrentTime():
    currentTime = time.time()  # Get current time currentTime
    # Obtain the total seconds since midnight, Jan 1, 1970
    totalSeconds = int(currentTime)
    # Get the current second
    currentSecond = totalSeconds % 60
    # Obtain the total minutes
    totalMinutes = totalSeconds // 60
    # Compute the current minute in the hour
    currentMinute = totalMinutes % 60
    # Obtain the total hours
    totalHours = totalMinutes // 60
    # Compute the current hour
    currentHour = totalHours % 24
    # Display results

    currentMinute = str(currentMinute)
    currentMinute = currentMinute if len(str(currentMinute)) != 1 else "0" + currentMinute

    currentHour = str(currentHour)
    currentHour = currentHour if len(str(currentHour)) != 1 else "0" + currentHour

    currentSecond = str(currentSecond)
    currentSecond = currentSecond if len(str(currentSecond)) != 1 else "0" + currentSecond

    return currentHour + ":" + currentMinute + ":" + currentSecond + " GMT"
