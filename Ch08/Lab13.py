def prefix(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return

    result = ""
    index = 0
    while True:
        if index == (len(s1) - 1) or index == (len(s2) - 1):
            break
        if s1[index] == s2[index]:
            result += s1[index]
        else:
            break

        index += 1

    if len(result) != 0:
        print(result)


if __name__ == '__main__':
    print("distance", "disinfection", "  = ", end=" ")
    prefix("distance", "disinfection")
