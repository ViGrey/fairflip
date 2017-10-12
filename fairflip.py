import random
import sys

heads_percent = int(sys.argv[1])

while heads_percent > 0 and heads_percent < 100:
    f1 = heads_percent > random.randint(0, 100)
    f2 = heads_percent > random.randint(0, 100)
    if f1 != f2:
        if f1:
            print("HEADS")
        else:
            print("TAILS")
        break
