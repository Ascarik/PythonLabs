def countLetters(s: str) -> int:
    count = 0
    for i in range(len(s)):
        if s[i].isalpha():
            count += 1

    return count


if __name__ == '__main__':
    s = "Welcome"
    print(s, countLetters(s))

    s = "W"
    print(s, countLetters(s))
