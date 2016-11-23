import random
prob1 = 0
prob2 = 0
prob3 = 0
prob4 = 0
mil = 1000000

for i in range(0,mil):
    r = random.randint(1,100)

    if r<=50:
        prob1 +=1
    elif r>50 and r<50+12.5:
        prob2 +=1
    elif r>=50+12.5 and r<=75:
        prob3 +=1
    else:
        prob4 +=1

print("probability1 is", prob1/mil)
print("probability2 is", prob2/mil)
print("probability3 is", prob3/mil)
print("probability4 is", prob4/mil)