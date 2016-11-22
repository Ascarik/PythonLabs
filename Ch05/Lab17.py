count = 0
for i in range(ord("!"), ord("~")):
    print(chr(i), end=" ")
    count += 1
    if count == 10:
        print()
        count = 0
