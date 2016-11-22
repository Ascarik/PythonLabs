import random


def getScissorRockPaper(my_num):
    if my_num == 0:
        name = "scissor"
    elif my_num == 1:
        name = "rock"
    else:
        name = "paper"
    return name


computer = 0
user = 0

while True:

    my_num = random.randint(0, 2)

    random_num = random.randint(0, 2)
    result = "The computer is {0}. You are {1}".format(getScissorRockPaper(random_num),
                                                       getScissorRockPaper(my_num))

    if my_num == random_num:
        result += " too. It is a draw."
    elif my_num == 0 and random_num == 2:
        result += ". You won."
        user += 1
    elif my_num == 0 and random_num == 1:
        result += ". You lost."
        computer+=1
    elif my_num == 1 and random_num == 0:
        result += ". You won."
        user += 1
    elif my_num == 1 and random_num == 2:
        result += ". You lost."
        computer += 1
    elif my_num == 2 and random_num == 0:
        result += ". You lost."
        computer += 1
    elif my_num == 2 and random_num == 1:
        result += ". You won."
        user += 1

    print(result)

    if user==2 or computer==2:
        break


if user==2:
    print("User won")
else:
    print("Computer won")