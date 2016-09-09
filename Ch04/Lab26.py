num = int(input("Enter a three-digit integer: "))

pali = num // 100

pali = ((num % 100) // 10) * 10 + pali

pali = ((num % 100) % 10) * 100 + pali

print(num, "is a palindrome" if pali == num else "is not a palindrome")
