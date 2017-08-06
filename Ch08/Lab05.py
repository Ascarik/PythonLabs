def count(fullstring: str, substring: str) -> int:
    sequence = 0

    if len(substring) > len(fullstring):
        return sequence

    index = 0
    i = 0

    while i < len(fullstring) or index < (len(fullstring) - i):

        while fullstring[i] == substring[index]:
            if index + 1 == len(substring):
                sequence += 1
                index = 0
                break

            index += 1
            i += 1

        i += 1

    return sequence


if __name__ == '__main__':
    str2 = "error"
    str1 = "system error, syntax error"
    print("'{0}' and '{1}' : {2}".format(str1, str2, count(str1, str2)))

    str2 = "error1"
    str1 = "system error, syntax error"
    print("'{0}' and '{1}' : {2}".format(str1, str2, count(str1, str2)))

    str2 = "err"
    str1 = "system error, syntax error"
    print("'{0}' and '{1}' : {2}".format(str1, str2, count(str1, str2)))

    str2 = "syntax"
    str1 = "system error, syntax error"
    print("'{0}' and '{1}' : {2}".format(str1, str2, count(str1, str2)))

    str2 = "r"
    str1 = "system error, syntax error"
    print("'{0}' and '{1}' : {2}".format(str1, str2, count(str1, str2)))
