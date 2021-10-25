# Rishi Motupalli
# Arithmetic Operators
# + - * / (% - mod(used for remainder))
#check for even numbers
import os
os.system('cls')
num = int(input("Enter a number:"))
rem = num%2
#conditional
if rem == 0:
    print("Your number is even")
else: 
    print("Your number is odd")