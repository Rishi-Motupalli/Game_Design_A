# Rishi Motupalli
# 9/13/21

import os
os.system('cls')


random = (input("Enter anything:")) # typecast any variable type to test this out
print(random)
try:
    int(random)
    check=True
except ValueError:
    check = False

if (check):
    # I will be back
    print()
else:
    print(len(random))

for i in random:
    print(i)

if len(random>3):
    print(random[3])










# if((type(random)) == int):
#     print("you gave me an integer")
# else: 
#     print("your input is not an integer")




