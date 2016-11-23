count = 0
for i in range(1, 8):
    for j in range(1, 8):
        if i != j:
            if j > i:
                print(i, j)
                count += 1

print("The total number of all combinations is", count)
