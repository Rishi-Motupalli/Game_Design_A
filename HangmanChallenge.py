# Make a hangman game that reveals letters one at a time
# Need to limit tries

import random, os 
os.system('cls')

def updateWord(word, guesses): #function to update dashes and letters
        for letters in myFruit:
            if letters in myFruit:
                print(letters, end = '')
            else: 
                print('_', end = '')


def Menu():
    print("############################################")
    #put instructions here
    print("#                Menu                      #")
    print("#                                          #")
    print("#              1. Animals                  #")
    print("#              2. Computer Parts           #")
    print("#              3. Fruits                   #")
    print("#              4. Exit                     #")
    print("#  To play, select 1 - 3, to exit select 4 #")
    print("############################################")
    print ()
    sel = input("What would you like to do?")
    #Try and except
    sel =int(sel)
    return sel
def selWord():
    if sel == 1:
        myFruit = random.choice(animals)
    elif sel == 2:
        myFruit = random.choice(computerParts)
    else:
        myFruit = random.choice(mylist)



animals = ["tiger, elephant, lion, giraffe, zebra"]
mylist = ["apple", "grape", "lemon", "peach"]
computerParts = ["keyboard", "monitor" ]










mylist = ["apple", "grape", "lemon", "peach"]
print("Hello")
name = input("What is your name?")
answer = input(name+", Do you want to play a game of hangman with fruits? y/n")
counter = 0
sel = Menu()

while sel != 4:
    print(name, " Good Luck! you have 5 chnaces")
    turns = 5
    counter += 1
    myfruit = selWord()
    myFruit = myFruit.lower()
    guesses = ''
    letcount = 0
    wordCount = len(myFruit)
    # print(myFruit) # just for checking if it works
    guesses = ''
    for letters in myFruit:
        if letters in myFruit:
            print(letters, end = '')
        else: 
            print('_', end = '')
    while turns > 0 and letcount <= wordCount :
        print()
        newguess = input(name + " Give me a letter") 
        newguess = newguess.lower
        if newguess in myFruit:
            guesses += newguess
            letcount += 1
            print("You guessesd a letter")
        else:
            turns -= 1
            print("Sorry, you have", turns, "left")

        for letters in myFruit:
            if letters in myFruit:
                print(letters, end = '')
        else: 
            print('-', end = '')
          
    answer = input(name + "Do you want to play again")

