s = int(input("Enter an integer:"))
result = ''
result += str(s % 10)
s = s // 10
result += str(s % 10)
s = s // 10
result += str(s % 10)
s = s // 10
result += str(s % 10)
print("The reversed number is", result)
