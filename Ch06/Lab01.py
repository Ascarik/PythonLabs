def getPentagonalNumber(n):
    return n * (3 * n - 1) / 2

for i in range(1, 11):
    print("PentagonalNumber(", i, ") = ", getPentagonalNumber(i))
