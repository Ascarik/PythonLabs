import random


def getScissorRockPaper(my_num):
    if my_num == 0:
        name = "scissor"
    elif my_num == 1:
        name = "rock"
    else:
        name = "paper"
    return name


my_num = int(input("scissor (0), rock (1), paper (2): "))

random_num = random.randint(0, 2)
result = "The computer is {0}. You are {1}".format(getScissorRockPaper(random_num),
                                                   getScissorRockPaper(my_num))

if my_num == random_num:
    result += " too. It is a draw."
elif my_num == 0 and random_num == 2:
    result += ". You won."
elif my_num == 0 and random_num == 1:
    result += ". You lost."
elif my_num == 1 and random_num == 0:
    result += ". You won."
elif my_num == 1 and random_num == 2:
    result += ". You lost."
elif my_num == 2 and random_num == 0:
    result += ". You lost."
elif my_num == 2 and random_num == 1:
    result += ". You won."

print(result)
