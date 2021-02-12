#This lab is a guess the number game

#importing random number values
import random


#code to create random numbers
print("Guess a random number between 0 and 10")
myNumber = int(input())
myRandomNumber = (random.randint(0, 10))
#if and else if statements within a while loop
while myNumber != myRandomNumber:
    if myNumber < myRandomNumber:
        print("Too Low, try again")
        myNumber = int(input())
    elif myNumber > myRandomNumber:
        print("Too High, try again")
        myNumber = int(input())
    elif myNumber == myRandomNumber:
        print("You did it!")
        mynumber = int(input())   
    else:
        print("Not a valid input, try again")
#final output
print("The random number is %s " % (myRandomNumber))
