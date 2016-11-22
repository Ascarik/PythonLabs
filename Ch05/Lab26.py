sum = 0
step = 1
for i in range(3, 100, 2):
    sum += step / i
    step += 2

print("sum =", sum)
