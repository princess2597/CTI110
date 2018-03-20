#CTI - 110
#P4HW2: Running Total 
#Toneshia Ried
#March 20, 2018

total = 0
userNumber = float( input("Enter a number? "))

while userNumber > -1:
    total = total + userNumber
    userNumber = float(input("Enter a number? "))

print("\nTotal:",total)
