def decimalToBinary(decimal: str) -> str:
    number = ""
    length = len(decimal)
    decimal = int(decimal)
    while decimal > 0:
        num = decimal % 2
        decimal = int(decimal / 2)
        number = str(num) + number

    return number


if __name__ == '__main__':
    # 895 = 0000001101111111b
    print("895", "=", decimalToBinary("895"))
