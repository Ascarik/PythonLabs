PI = 1
flag = True

for i in range(1, 10, 2):
    if flag:
        PI -= 1 / (i + 2)
        flag = False
    else:
        PI += 1 / (i + 2)
        flag = True

PI *= 4

print("Approximate Pi:", PI)
