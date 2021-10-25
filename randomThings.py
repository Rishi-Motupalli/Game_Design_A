# Rishi Motupalli
# 9/15/21
# We are going to learn how to use random numbers
# Make a number guessing game
import os
import random

os.system('cls')
random.seed(20)
#This loop was used to play with random
for i in range(10):
    rando = random.randint(3,5) 
    #print(rando)
    rando2 = random.random()
    rando2 *=100
    #print(rando2)
    print(int(rando2))


# Arrays in python are called lists
fruits = ["apple", "banana", "orange"]
myFruit = random.choice(fruits)
print(myFruit)