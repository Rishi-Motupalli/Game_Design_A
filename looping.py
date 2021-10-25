#Rishi Motupalli
# 09/07/2021
# we are going to learn how to use loops
# Ask user for the number of stars (input)
# Loop (repeat number of times)
# print ("*")

star = int(input("How many stars are there?"))
# input always gives you a string
# switching the type of data = type casting
print(star, "stars")
line=star
for i in range(line):
    for space in range(i):
        print(" ", end=" " )
    # add a loop for the spaces
    for counter in range(star): # you can use a number or variable
        print("*", end=" " ) # prints on the same line
        # print(counter+1, end=" ")
    print() #print a return to start a new line
    star -= 1 # shortcut for star = star-1
print("Thank you!")


