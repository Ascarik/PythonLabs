# Converts from feet to meters
def footToMeter(foot):
    return 0.305 * foot


# Converts from meters to feet
def meterToFoot(meter):
    return meter / 0.305


print(
    format("Feet", "20s"), format("Meters", ">10s"),
    " | ", format("Meters", "20s"),
    format("Feet", ">10s"), end="\n\n"
)

feet = 1
meters = 20
for degree in range(0, 10):
    print(format(feet, "<20.1f"), format(footToMeter(feet), "10.2f"),
          " | ", format(meters, "<20.1f"), format(meterToFoot(meters), ">10.2f"))
    feet += 1
    meters += 6
