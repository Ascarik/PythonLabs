def reverse(s: str) -> str:
    str_result = ""
    for i in range(len(s) - 1, -1, -1):
        str_result += s[i]

    return str_result


if __name__ == '__main__':
    s = "welcome"
    print(s, reverse(s))
