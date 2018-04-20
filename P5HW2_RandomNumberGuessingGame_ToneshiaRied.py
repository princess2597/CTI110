#CTI - 110
#P5HW2 Random Number Guessing Game
#Toneshia Ried
#April 20, 2018

import random

def generateRandomNumber():
    randomNumber = random.randint( 1, 100)
    return randomNumber

def askUserForNumber( message = "Guess the number: " ):
    userNumber = int(input( message ))
    return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too High"
    elif userNumber < randomNumber:
        return "Too Low"
    else:
        return "Congratulations!"

def main():
    print()
    userCongratulated = False
    letsStart = True
    
    while userCongratulated or letsStart:
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        userNumber = askUserForNumber()
        userNumberOfGuesses += 1
        message = checkUserNumber( userNumber, randomNumber )

        while message != "Congratulations!":
            print( message )
            userNumber = askUserForNumber( "Try Again: " )
            userNumberOfGuesses = userNumberOfGuesses + 1
            message = checkUserNumber( userNumber, randomNumber )
            
        print ()
        print ( message, "It took you", userNumberOfGuesses, \
                "tries to guess the correct number.\n" )
        userCongratulated = True 

main()
