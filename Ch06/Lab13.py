def sunSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i / (i + 1)

    return sum


print(format("i", "10s"), "m(i)")
for i in range(1, 21):
    print(format(i, "<10d"), format(sunSeries(i), ".4f"))
