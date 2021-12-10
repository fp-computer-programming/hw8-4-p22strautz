# Author: SCT (AMDG) 12/9/21

import random

rannum = random.randint(0, 50)

while True:
    guess = (input("Guess a number from 0-50. "))
    if (guess) == "stop":
        break
    if(int(guess) > rannum):
        print("Lower!")
        continue
    elif(int(guess) < rannum):
        print("Higher!")
        continue
    elif(int(guess) == rannum):
        print("You guessed it right!")
    break
