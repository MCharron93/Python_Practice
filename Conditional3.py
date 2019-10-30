#
#
import random

#
#   Variables for dice sides
lower = 4
numSides = 4

#
#   Custom function: die roll for random number in between lower and
#   upper values. return results to call and print

def rollDie(lower, numSides):
    if numSides >= 1 and numSides < 64:
        results = random.randint(lower, numSides)
        return results
    else:
        print ("Number of sides should be between 0 and 64")
        #print (badResults)
        return badResults

#
#   Roll calls and stores for values for random output

yourRoll = rollDie(lower, numSides)
friendsRoll = rollDie(lower, numSides)


print("Player 1 rolled " + str(yourRoll) + ".")
print("Player 2 rolled " + str(friendsRoll) + ".")


#
#   Coin toss to determine tie breaks
#
#   Players must state their bets prior to the flip--> insert user input

heads = 0
tails = 1

input("Player 1 makes the call. Input a call, heads = 0, and tails = 1:")


def coinToss():
    tossResults = random.randint(heads, tails)
    if tossResults == 0:
        print ("It is heads")
    elif tossResults == 1:
        print ("It is tails")
    else:
        print ("The game is rigged. No one wins!")
    return tossResults
    

#
#   Insert conditional statements to determine winners
if yourRoll == 0:
    print ("ERROR. DOES NOT COMPUTE!")
elif yourRoll > friendsRoll:
    print ("Player 1 wins! " + str(yourRoll) + " to " + str(friendsRoll) + ".")
elif friendsRoll > yourRoll:
    print ("Player 2 wins! " + str(friendsRoll) + " to " + str(yourRoll) + ".")
else:
    print ("It's a tie! Ties must be broken with a coin toss!") 
    coinToss()

#
#   Print statements for players coin toss


