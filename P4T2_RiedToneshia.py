#CTI - 110
#P4T2: Bug Collector
#Toneshia Ried
#March 18, 2018

totalDays = 7
totalNumberOfBugs = 0
for currentDay in range(1, totalDays + 1):
    bugsCollected = int(input("How many bugs were collected on day" + str(currentDay)+ ": "))

    totalNumberOfBugs = totalNumberOfBugs + bugsCollected
print("\nThe total number of bugs collected for all 7 days is", totalNumberOfBugs)
