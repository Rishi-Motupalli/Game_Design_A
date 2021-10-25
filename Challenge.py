#Rishi Motupalli
# 09/07/2021
# we are going to learn how to use loops
# Ask user for the number of stars (input)
# Loop (repeat number of times)
# print ("*")
import os
os.system('cls')
star = int(input("How many stars are there?"))
line=star
space=0

print(star, "stars")

for i in range(line):
    for counter in range(star): # you can use a number or variable
        print("*", end=" " )
    
    for j in range (space):
        print(" ", end=" " )
    space += 2 # adds 2 instead of 1 for every space
    
    for counter in range(star): # you can use a number or variable
        print("*", end=" " ) # prints on the same line
        # print(counter+1, end=" ")
    print() #print a return to start a new line
    star -= 1 # shortcut for star = star-1
    
