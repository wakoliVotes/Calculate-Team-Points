# This functions works by taking wins, draws and losses and computing a teams total points
# In this scenario, a win = 3 points, a draw = 1 point and a loss = 0 points
onesTeamName = input("Enter the Name of your name : ")
wonMatches = input("Kindly enter the number of matches your team won :  ")
if float(wonMatches) >= 40:
    print("Error, please enter a valid number")
drawMatches = input("Kindly enter the number of matches your team draw :  ")
if float(drawMatches) >= 40:
    print("Error, please enter a valid number")
lossMatches = input("Kindly enter the number of matches your team lost :  ")
if float(lossMatches) >= 40:
    print("Error, please enter a valid number")
if float(wonMatches + drawMatches + lossMatches) >= 40:
    print("You entered too many items or wrong values for your team.")
teamPoints = float(wonMatches)* 3 + float(drawMatches)*1 + float(lossMatches)*0
print("The Total Points for " + onesTeamName + " this 2021 Season is :: ", teamPoints)
if teamPoints >= 100:
    print("You have Broken the record and are the champions.")
elif teamPoints >= 80:
    print("Your Team is in the 2nd Place")
elif teamPoints >= 60:
    print("Your team  " +  onesTeamName +" is in the 3rd Place.")
else:
    print("Its Amazing for the journey, however, Your " + onesTeamName +" is NOT in the TOP 4 this year.")