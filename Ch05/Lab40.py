import random

head = 0
tail = 0
for i in range(0, 1000000):
    if random.randint(0, 1) == 0:
        tail += 1
    else:
        head += 1

print("heads =", head)
print("tails =", tail)
