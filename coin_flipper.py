import random

flips = 0
heads = 0
tails = 0
while flips < 100:
    if random.randint(1, 2) == 1:
        print("heads")
        heads += 1
    else:
        print("tails")
        tails += 1
    flips += 1

print("you got", heads, "heads. and", tails, "tails")
input("done c:")
