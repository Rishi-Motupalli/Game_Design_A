

 #09/29/2021
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word

import random, os
os.system('cls')


#function to update dashes and letters
def updateWord(word, guesses, letCount):
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
            letCount+=1
        else:
            print('_', end=' ')
    return letCount

def Menu():
    print("########################################")
    print("#                MENU                  #")
    print("#                                      #")
    print("#       1. Animals                     #")
    print("#       2. Computer Parts              #")
    print("#       3. Fruits                      #")
    print("#       4. ScoreBoard                  #")
    print("#       5. Exit                        #")
    print("########################################")
    print()

    while 1:
        sel=input("What would you like to do?")
        try:
            sel = int(sel)
            break
        except ValueError:
            print("this is not an integer")   # excepting classes (ints)
    return sel
    
def selWord(sel): 
                   # function to detirmine the outcome of what the user chooses
    if sel == 1:   
        word= random.choice(animals)
    elif sel == 2:
        word= random.choice(compParts)
    elif sel == 3: 
        word= random.choice(fruits)
   # elif sel == 4:
    #    myFile= open('score.txt','r')
     #   print(myFile.read())  
      #  myFile.close() #closes file
        #print()
    #elif sel == 5:
     #   print("Thank your for playing!")
      #  print (name + "\t Highest score:\t"+str(maxScore))
       # os._exit
    return word


animals=["tiger", "elephant", "turtle", "chicken", "mouse", "monkey"] #listsm
fruits=["bananas", "strawberries", "apples","peaches", "oranges", "pears" ]
compParts=["keyboard", "Monitors", "computer","trackpad", "case","OperatingSystem"]

name= input("What is your name? ")
maxScore=0 #to store highest Score
sel = Menu() #calling the menu function
print(sel)


    
while sel==1 or sel==2 or sel==3:   
   
            word= selWord(sel)
            word = word.lower() # making the word lower case
            wordCount=len(word)
            turns= wordCount+2  # depending on the length if the word
            letCount=0 # variable to check if the user guessed the word
            print(word) # just for checking our code delete later
            guesses=''
            score=0
            letCount=updateWord(word, guesses, letCount)

    while turns > 0 and letCount<wordCount:
        print()
        newguess=input (name + " Give me a letter ")
        newguess= newguess.lower()

        if newguess in word:
            guesses += newguess
            print("you guessed one letter ")

        else:
            turns -=1
            print("Sorry, you have ", turns, "turns left")
            letCount=0
            letCount= updateWord(word, guesses, letCount) # calling a function
                
    if turns > 0 :
        print(" ")
        print("you win!!")
        score += 1
        print(score)

    else:
        print("you lose...try again") # using a conditional statement for an uncertain outcome
        score = score
        score=3*wordCount+5*turns

    if score > maxScore: # determining whether a score is the new high score
        maxScore=score
        print(maxScore)
        os.system('cls') # clearing the bottom area
        sel=Menu()

myFile = open('score.txt','w')          # writing in a file 'score.txt'
myFile.write (str(maxScore))            ## print(myFile.read())
myFile.close()         

if sel == 4:
    myFile = open("scoreboard.txt", "r") # reading the file
    print(myFile.read())                 # reading and printing file
    myFile.close()

if sel == 5:    
    print(name + ": " + str(maxScore))  # adding new score with name
    os._exit


