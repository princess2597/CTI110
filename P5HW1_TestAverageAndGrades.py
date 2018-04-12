#This project will calculate test score for each of 5 students and the average grade of those 5.
#CTI - 110
#P5HW1_TestAverageAndGrades
#Toneshia Ried
#April 12, 2018


def calculateAverage( test1, test2, test3, test4, test5 ):
    averageTest = ( test1 + test2 + test3 + test4 + test5) / 5

def grade( studentScore):
    if(studentScore < 60 ):
        return "F"
    elif(studentScore < 70):
        return "D"
    elif(studentScore < 80):
        return "C"
    elif(studentScore < 90):
        return "B"
    elif(studentScore <101):
        return "A"

def requestScore():
    test1 = float( input('Enter first score: ' ))
    test2 = float( input('Enter second score: ' ))
    test3 = float( input('Enter third score: ' ))
    test4 = float( input('Enter fourth score: ' ))
    test5 = float( input('Enter fifth score: ' ))

    return test1, test2, test3, test4, test5

def results( test1, test2, test3, test4, test5):
    print("\nScore\tLetter Grade" )
    print()
    print( str(test1) + "\t\t" + grade( test1), \
           str(test2) + "\t\t" + grade( test2), \
           str(test3) + "\t\t" + grade( test3), \
           str(test4) + "\t\t" + grade( test4), \
           str(test5) + "\t\t" + grade( test5), sep ="\n")
    print()
    print( "The Average Score is", (test1 + test2 + test3 + test4 + test5) / 5)

def main():
    test1, test2, test3, test4, test5 = requestScore()
    results(test1, test2, test3, test4, test5)

main()

