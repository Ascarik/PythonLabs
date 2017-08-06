from Ch08.Lab08 import binaryToDecimal


def binaryToHex(binaryValue: str) -> str:
    decimal = binaryToDecimal(binaryValue)
    number = ""
    while decimal != 0:
        num = decimal % 16
        decimal = int(decimal / 16)
        if num > 9:
            number = chr((ord("A") - 10) + num) + number
        else:
            number = str(num) + number

    return number


if __name__ == '__main__':
    # 0000001101111111 = 895 = 37F
    print("0000001101111111", "=", binaryToHex("0000001101111111"))
