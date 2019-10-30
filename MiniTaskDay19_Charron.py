#
# Author: Michelle Charron 
# Date: 10/30/2019
# Description:  Madlib random list generation
#
# This Madlib will require the following categories
#  adj  - http://examples.yourdictionary.com/examples-of-adjectives.html
#  noun  - http://examples.yourdictionary.com/noun-examples.html
#  adverb  - http://examples.yourdictionary.com/examples-of-adverbs.html
#  exclamation  - http://examples.yourdictionary.com/examples-of-interjections.html

import random
               
#
# This function is an implementation of the <REPLACE WITH MADLIB NAME> Madlib.
#   It will dynamically generate a new Madlib each time it is called by
#   randomly selecting values from the above lists
# Return
# This function will return a String containing the new Madlib
def generateMadlib():
    # Step 1. Define List variables for each category in your Madlib.  
    #    Add additional lists as necessary.
    ADJ_LIST = ["saggy", "spoopy", "smol", "annoying", "creepy", "swanky"]
    NOUN_LIST = ["Fart", "Doge", "Dingdong", "Sponge", "Drag Queen", "Dingus"]
    ADVERB_LIST = ["gently", "frantically", "then", "vigorously", "angerly" ]
    EXCLAMATION_LIST = ["Great scott!", "Whot en whut?!", "YeeHAW!", "Swiggity swoogity"]

    # Setup the output string that will contain the Madlib
    output = ""

    # Step 2. Write your Madlib below using String concatenation and the random.choice() function
    output += "In a galaxy far, far away. . . " + random.choice(NOUN_LIST) 
    output += " was on a " + random.choice(ADJ_LIST) + " quest to find the " + random.choice(ADJ_LIST)+ " "
    output += random.choice(NOUN_LIST) + ". Little did they know that the " + random.choice(ADJ_LIST) + " "
    output += random.choice(NOUN_LIST) + " would be " + random.choice(ADVERB_LIST) + " waiting to attack. "
    output += random.choice(EXCLAMATION_LIST) + " they yelled, as their attack commenced."

    # Return generated Madlib
    return output




#
# Generate the Madlib
#
madlib = generateMadlib()

#
# Print the Madlib
#
print(madlib)


