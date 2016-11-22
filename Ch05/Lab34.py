import random

# Generate a lottery number
lottery = random.randint(10, 99)

while True:
    guessDigit1 = random.randint(1, 9)
    guessDigit2 = random.randint(1, 9)
    if guessDigit1 != guessDigit2:
        break

guess = guessDigit1*10 + guessDigit2
# Get digits from lottery
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

print("The lottery number is", lottery)
print("The guess number is", guess)

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guessDigit2 == lotteryDigit1 and \
                  guessDigit1 == lotteryDigit2):
    print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1
      or guessDigit1 == lotteryDigit2
      or guessDigit2 == lotteryDigit1
      or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
