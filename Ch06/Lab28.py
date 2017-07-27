import random


def isWin(num1, num2):
    sum = num1 + num2
    if sum == 11 or sum == 7:
        return True
    return False


def isLose(num1, num2):
    points = [2, 3, 12]
    sum = num1 + num2
    if sum in points:
        return True
    return False


def isWinPoint(num1, num2, point):
    sum = num1 + num2
    if sum == point:
        return True
    return False


flag = True
point = 0
sumCraps = 0
while True:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    print("You rolled {} + {} = {}".format(num1, num2, num1 + num2))

    if isWin(num1, num2) and flag:
        print("You win")
        break

    elif isLose(num1, num2) and flag:
        print("You lose")
        break

    if flag:
        flag = False
        sumCraps = num1 + num2
        print("Point is {}".format(num1 + num2))
    else:
        if sumCraps == num1 + num2:
            print("You win")
            break
        else:
            print("You lose")
            break
