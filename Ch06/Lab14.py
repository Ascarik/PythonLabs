from math import pow


def estimatePI(n):
    sum = 0
    for i in range(1, n + 1):
        sum += pow(-1, i + 1) / (2 * i - 1)

    return sum * 4


print(format("i", "10s"), "m(i)")
for i in range(1, 1000, 100):
    print(format(i, "<10d"), format(estimatePI(i), ".4f"))
