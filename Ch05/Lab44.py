import random

decimal = random.randint(100, 1001);

binary = ""
resultdec = decimal

while True:
    binary = str(decimal % 2) + binary
    decimal //= 2
    if decimal == 0:
        break

print(resultdec, "=", binary)
