import random

decimal = random.randint(100, 1001);

hex = ""
resultdec = decimal

while True:
    num = decimal % 16
    if num > 10:
        num = chr(num + 55)
    hex = str(num) + hex
    decimal //= 16
    if decimal == 0:
        break

print(resultdec, "=", hex)
