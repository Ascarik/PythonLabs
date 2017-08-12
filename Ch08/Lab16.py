def card13_validation(isbn: str) -> str:
    if len(isbn) != 12:
        return ""

    sum = 0
    for i in range(len(isbn)):
        if i % 2 == 0:
            sum += int(isbn[i])
        else:

            sum += int(isbn[i]) * 3

    if (10 - sum % 10 == 10):
        isbn += "0"
    else:
        isbn += str(10 - sum % 10)

    return isbn


if __name__ == '__main__':
    isbn = "978013213080"
    print("{} = {}".format(isbn, card13_validation(isbn)))
    isbn = "978013213079"
    print("{} = {}".format(isbn, card13_validation(isbn)))
