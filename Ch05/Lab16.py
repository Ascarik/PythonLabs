def gcd(a, b):
    return a if b == 0 else gcd(b, a % b);


print("gcd =", gcd(252, 198))
