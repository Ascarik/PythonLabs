def reverse(number):
    revResult = ""
    while number > 0:
        revResult += str(number % 10)
        number //= 10
    return revResult


def isPalindrome(number):
    return str(number) == reverse(number)


print("Is 235 palindrome", isPalindrome(235))
print("Is 838 palindrome", isPalindrome(838))
