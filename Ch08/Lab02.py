def find(substring: str, fullstring: str) -> bool:
    '''
    Check substrings

    :param substring: substring
    :param fullstring: string
    :return: True if str1 is a substring of str2, unless False
    '''
    if len(substring) > len(fullstring):
        return False

    index = 0
    i = 0
    while i < len(fullstring) or index < (len(fullstring) - i):

        while fullstring[i] == substring[index]:
            if index + 1 == len(substring):
                return True

            index += 1
            i += 1

        i += 1

    return False


if __name__ == '__main__':
    str1 = "elco"
    str2 = "Welcome"
    print("{0} and {1} is {2}".format(str1, str2, find(str1, str2)))

    str1 = "etlco"
    str2 = "Welcome"
    print("{0} and {1} is {2}".format(str1, str2, find(str1, str2)))

    str1 = "Welco"
    str2 = "Welcome"
    print("{0} and {1} is {2}".format(str1, str2, find(str1, str2)))

    str1 = "come"
    str2 = "Welcome"
    print("{0} and {1} is {2}".format(str1, str2, find(str1, str2)))

    str1 = "o"
    str2 = "Welcome"
    print("{0} and {1} is {2}".format(str1, str2, find(str1, str2)))
