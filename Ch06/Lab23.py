def convertMillis(millis):
    seconds = (millis // 1000) % 60
    minutes = ((millis // 1000) // 60) % 60
    hours = ((millis // 1000) // 60) // 60

    print("{}:{}:{}".format(hours, minutes, seconds))


convertMillis(5500)

convertMillis(100000)

convertMillis(555550000)
