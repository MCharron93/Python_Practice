#   Author: Michelle Charon
#   Date:11/6/2019
#   Description:    Retro Arcade game. User is prompted for name input. Player picks games that cost credits, beginning with 100 credits initially. 
#                   Menu options allow players to pick games and generate madlibs to change their credit totals. Winner banners initialize when a 
#                   player, or computer, has won. 
#
#

import random

#
#
#   Game of Dice

lower = 1
numSides = 6

#
#   Custom function: die roll for random number in between lower and
#   upper values. return results to call and print

def rollDie(player):
    
    #   Welcome Message 
    print("\nHello " + player + " welcome to the Dice Game!")
    print("\nThe current scores begin at 0, you play against the Computer. Each player rolls a die and the higher roll wins.")
    print("The first player to 5 round wins, wins the game.")
    
    #   Player beginning scores
    playerScore = 0
    compScore = 0

    #   While loop rolls the die AND increases scores
    
    while playerScore < 5 and compScore < 5:

        print("\nScoreboard: ")
        print(playerScore)
        print(compScore)

        input("Please press ENTER to roll. . . ")

        yourRoll = random.randint(lower, numSides)
        compRoll = random.randint(lower, numSides)

        if yourRoll > compRoll:
            playerScore = playerScore + 1
        elif compRoll > yourRoll:
            compScore = compScore + 1
        else:
            compScore = compScore + 1

    #  Determining the winner
    if playerScore > compScore:
        print("Scoreboard: ")
        print(playerScore)
        print(compScore)
        return True
    else:
        print("Scoreboard: ")
        print(playerScore)
        print(compScore)
        return False
    
#
#
#   Lucky Slots Game

#
#   Custom function: pull slots for random generation of outcomes
#   with multiple listed items in sets

def pullSlot(player):

    #   Welcome message for the player
    print("\nHello " + player + " welcome to Lucky Slots Game! Try your luck at getting 3 symbols in a row!")
    print("You are playing against the Computer, so lets test your odds!")

    #   List of aymbols in the slots
    symbolList = ["Cherry", "Diamond", "Heart", "Star", "Seven", "Jack", "Queen", "Spade", "King", "Mushroom"]

    #   Player beginnging attempts
    attempts = 0

    #   While Loop for attempted pulls
    while True:

        input("\nPlese press ENTER to pull the bar. . . ")

        yourRow1 = (random.choice(symbolList))
        yourRow2 = (random.choice(symbolList)) 
        yourRow3 = (random.choice(symbolList))

        output = "\nRow 1:" + yourRow1
        output += "\nRow 2:" + yourRow2
        output += "\n Row 3: " + yourRow3

        print(output)

        if yourRow1 == yourRow2 and yourRow1 == yourRow3:
            print("\nAll of your symbols match! You are extra lucky today!")
            return True
        else:
            print("\nIf all 3 match in a row, you are extra lucky today!")

    #   Make loop for variable to add attempts every pull and condition for breaking out of while loop 
        attempts = attempts + 1
        print("\nAttempts: " + str(attempts))
        
        if attempts < 5:
            print("Please pull again, you have attempted " + str(attempts) + " pull(s) so far!")
        elif attempts >= 5:
            print("Thank you for playing Lucky Slots!")
            break 
        else:
            print("The game is rigged, better luck next time!")
            

#
#
#   Madlib Game

#
#
#   Custom function for Madlib generation

def generateMadlib(player):

    #   Greeting message for game
    print("\nHello " + player + " welcome to Madlibs!\nCreate your own story and see what adventures lie ahead!")

    #   List of values
    ADJ_LIST = ["saggy", "spoopy", "smol", "annoying", "creepy", "swanky"]
    NOUN_LIST = ["Fart", "Doge", "Dingdong", "Sponge", "Drag Queen", "Dingus"]
    ADVERB_LIST = ["gently", "frantically", "then", "vigorously", "angerly" ]
    EXCLAMATION_LIST = ["Great scott!", "Whot en whut?!", "YeeHAW!", "Swiggity swoogity"]

    # Setup the output string that will contain the Madlib
    output = ""

    # Step 2. Write your Madlib below using String concatenation and the random.choice() function
    output += "\nIn a galaxy far, far away. . . " + random.choice(NOUN_LIST) 
    output += " was on a " + random.choice(ADJ_LIST) + " quest to find the " + random.choice(ADJ_LIST)+ " "
    output += random.choice(NOUN_LIST) + ". Little did they know that the " + random.choice(ADJ_LIST) + " "
    output += random.choice(NOUN_LIST) + " would be " + random.choice(ADVERB_LIST) + " waiting to attack. "
    output += random.choice(EXCLAMATION_LIST) + " they yelled, as their attack commenced!"

    # Return generated Madlib
    return output

#
#
#   display if Player or Computer Wins
def displayWinner(player):
    winnerString = "* " + player + " Wins! *" 
    starBorder = "*" * len(winnerString)
    print(starBorder)
    print(winnerString)
    print(starBorder)

#
#
#   Start Game Menus

balance = 100

print("Hello, welcome to Retro Arcade! We have many fun games to be played.") 
player = input("\nplease enter your name: ")
computer = "Computer"


#   
#
#   Game Menu and Options

endGame = False

while endGame == False:
    response = input("\nYou begin the game with 100 credits! Please select a game option: D = Dice -10 credits, S = Slots -10, M = Madlib +20, Q = Quit: ")
    if response.lower() == "d":
        balance = balance - 10
        playerWins = rollDie(player)
        if (playerWins == True):
            displayWinner(player)
        else:
            displayWinner(computer)
        print("\nYour balance is now " + str(balance) + " credits.")
    elif response.lower() == "s":
        balance = balance - 10
        playerWins = pullSlot(player)
        if (playerWins == True):
            displayWinner(player)
        else:
            displayWinner(computer)
        print("\nYour balance is now " + str(balance) + " credits.")
    elif response.lower() == "m":
        balance = balance + 20
        madlib = generateMadlib(player)
        print(madlib)
        print("\nYour balance is now " + str(balance) + " credits.")
    elif response.lower() == "q":
        endGame = True
        print("\nThank you for playing Retro Arcade. Your final balance is: " + str(balance) + " credits. Please come again!")
    else:
        print("please make a selection: ")

