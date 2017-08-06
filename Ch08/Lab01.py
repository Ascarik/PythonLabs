def check_snn(snn: str) -> str:
    if len(snn) != 11:
        return "Invalid SNN"

    snn_without_underscores = snn.replace("-", "")

    if len(snn_without_underscores) == 9 and snn_without_underscores.isdigit():
        return "Valid SNN"

    return "Invalid SNN"


if __name__ == '__main__':
    snn = input("Enter SNN number: ")
    print(check_snn(snn))
