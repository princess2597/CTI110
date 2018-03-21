#CTI - 110
#P4HW3: Factorial
#Toneshia Ried
#March 21, 2018


userInteger = int(input("Enter a number:"))

while userInteger < 1:
    userInteger = int(input("Enter a non negative integer: "))

factorial = 1
    
for currentNumber in range(1, userInteger + 1):
    factorial = factorial * currentNumber

print("\nThe factorial of", userInteger, "is", factorial)
