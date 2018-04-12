#CTI - 110
#P5T2_FeetToInches
#Toneshia Ried
#April 12, 2018

def feetToInches(userFeet):
    inches =(userFeet / 1 ) * 12
    return inches

def main():
    userFeet = int(input('Enter a number of feet: '))
    inches = feetToInches(userFeet)
    print( userFeet, "feet converted to inches is", (format(inches, ".2f" )\
    , "inches"))

main()
