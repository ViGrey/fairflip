import random
import sys

heads_percent = int(sys.argv[1]) # Integer value of argument

while heads_percent > 0 and heads_percent < 100: # Loop if valid heads_percent
    # If random number is under heads_percent, then flip is HEADS
    flip1 = heads_percent > random.randint(0, 100) # True if HEADS result
    flip2 = heads_percent > random.randint(0, 100) # True if HEADS result
    if flip1 != flip2: # Restart loop if flip1 and flip2 are the same
        if flip1: # If first flip is HEADS, print HEADS
            print("HEADS")
        else: # If first flip is TAILS, print TAILS
            print("TAILS")
        break # break out of infinite loop
