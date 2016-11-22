count = 0
for i in range(2, 1001):
    if i % 5 == 0 or i % 6 == 0:
        print(i, end=" ")
        count += 1
        if count == 10:
            print()
            break