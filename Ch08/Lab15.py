def card_validation(isbn: str) -> str:
    if len(isbn) != 9:
        return ""

    sum = 0
    for i in range(len(isbn)):
        sum += (i + 1) * int(isbn[i])

    if (sum % 11 == 10):
        isbn += "X"
    else:
        isbn += str(sum % 11)

    return isbn


if __name__ == '__main__':
    isbn = "013601267"
    print("{} = {}".format(isbn, card_validation(isbn)))
    isbn = "013031997"
    print("{} = {}".format(isbn, card_validation(isbn)))
