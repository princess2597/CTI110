#CTI - 110
#P5T1_Kilometer Converter
#Toneshia Ried
#April 10, 2018




def askUserForKilometers():
    userKilometers = float( input("Enter the distance in kilometers:"))
    return userKilometers

def convertKilometersToMiles( userKilometers):
    miles = userKilometers * 0.6214
    return miles

def main():
    userKilometersTyped = askUserForKilometers()
    covertedMiles = convertKilometersToMiles(userKilometersTyped)

    print( userKilometersTyped, "kilometers converted to miles is",\
        format( covertedMiles, ".2f"), "miles")


main()

