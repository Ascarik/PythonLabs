def count(s: str, ch: str) -> int:
    ch_count = 0
    for i in range(len(s)):
        if s[i] == ch:
            ch_count += 1

    return ch_count


if __name__ == '__main__':
    s = "Welcome"
    print(count(s, "e"))
    s = "Welcome"
    print(count(s, "W"))
    s = "Welcome"
    print(count(s, "t"))
