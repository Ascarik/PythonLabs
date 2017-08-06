def binaryToDecimal(binaryString: str) -> int:
    sumbin = 0
    index = 0
    for i in range(len(binaryString) - 1, -1, -1):
        if binaryString[i] == "1":
            sumbin += 2 ** index

        index += 1
    return sumbin


if __name__ == '__main__':
    print("10001", "=", binaryToDecimal("10001"))
    print("11", "=", binaryToDecimal("11"))
    print("1101111111", "=", binaryToDecimal("1101111111"))
