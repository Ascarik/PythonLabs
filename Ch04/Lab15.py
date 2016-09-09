import random

lottery = random.randint(100, 999)

guess = eval(input("Enter your lottery pick (three digits): "))

lotteryDigit1 = lottery // 100
lotteryDigit2 = (lottery % 100) // 10
lotteryDigit3 = (lottery % 10) % 10
lotteryArray = [lotteryDigit1, lotteryDigit2, lotteryDigit3]

guessDigit1 = guess // 100
guessDigit2 = (guess % 100) // 10
guessDigit3 = (guess % 10) % 10

print("The lottery number is", lottery)
print("Your number is", guess)

if guess == lottery:
    print("Exact match: you win $10,000")

elif ((guessDigit1 in lotteryArray and guessDigit2 in lotteryArray) or
          (guessDigit2 in lotteryArray and guessDigit3 in lotteryArray) or
          (guessDigit1 in lotteryArray and guessDigit3 in lotteryArray)):
    print("Match all digits: you win $3,000")

elif (guessDigit1 in lotteryArray or
              guessDigit2 in lotteryArray or
              guessDigit3 in lotteryArray):
    print("Match one digit: you win $1,000")

else:
    print("Sorry, no match")
