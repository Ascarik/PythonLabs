def getNumber(uppercaseLetter: str) -> str:
    number = ""
    uppercaseLetter = uppercaseLetter.upper()

    for i in range(len(uppercaseLetter)):

        if uppercaseLetter[i].isalpha() and "A" <= uppercaseLetter[i] <= "Z":

            symbol = ord(uppercaseLetter[i]) - ord("A")

            if uppercaseLetter[i] != "S" and uppercaseLetter[i] != "Z":
                symbol = symbol // 3 + 2
            else:
                symbol = symbol // 3 + 1

            number += str(symbol)

        else:
            number += uppercaseLetter[i]

    return number


if __name__ == '__main__':
    print(getNumber("1-800-Flowers"))
    print(getNumber("1-800-ssssuz"))
