#CTI - 110
#P4HW1: Distance Traveled
#Toneshia Ried
#March 19, 2018

vehicleSpeed = float(input("What is the speed of the vehicle?"))
timeTraveled = int(input("How many hours has the vehicle traveled?"))

print( "Hour", "\tDistance Traveled" )
for currentHour in range(1, timeTraveled + 1):
    distanceTraveled = vehicleSpeed * currentHour
    print(currentHour,"\t",distanceTraveled)
