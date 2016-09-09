import random

suitArray = ["Clubs", "Diamonds", "Hearts", "Spades"]
rankArray = ["Ace", "Jack", "Queen", "King"]

rank = random.randint(2, 14)
suit = random.randint(0, 3)

if rank>10:
    rank = "the "+rankArray[rank-11]+" of"

suit = suitArray[suit]

print("The card you picked is {0} {1}".format(rank, suit))