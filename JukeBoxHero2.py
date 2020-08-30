#
#
#   Print Menu for Commands to Access Files

def printMenu():
    print("\n(L)oad Catalog")
    print("(S)earch Catalog")
    print("(A)nalyse Catalog")
    print("(P)rint Catalog")
    print("(Q)uit")


#
#
#   List Generator for Prompting User

def getListFromFile (inputFile):
    outputList = []
    try:
        source = open(inputFile,"r")
        outputList =  source.readlines()
        source.close()
    except FileNotFoundError:
        print("Unable to open input file: " + inputFile)

    return outputList

#
#
#   Catalog Load and Display

def printSong(songList):
    fullList = song.split(",")
    #print(fullList)
    
    artist = fullList[0]
    album = fullList[1]
    title = fullList[2]
    length = fullList[3]

    output = "\nArtist: " + artist
    output += "\nAlbum: " + album
    output += "\nTitle: " + title
    output += "\nLength: " + length + " seconds"

    print(output)

#
#
#   Find songs

def findSongs(queryTerm,songList):
    foundSongList = []
    for song in songList:
        if queryTerm.lower() in song.lower():
            foundSongList.append(song)

    return foundSongList
    
     

#
#   Catalog Analyse

def printCatalogStats():
    artistList = []
    albumList = []
    totalPlayTime = 0

    for song in songList:
        fieldList = song.split(",")

        artist = fieldList[0]

        if artist not in artistList:
            artistList.append(artist)

        album = fieldList[1]
        if album not in albumList:
            albumList.append(album)

        duration = fieldList[3]
        totalPlayTime += int(duration)

    print("Number of Artist: " + str(len(artistList))) 
    print("Name of Album: " + str(len(albumList)))
    print("Total Play Time: " + str(totalPlayTime) + " seconds.")

#
#
#   Greeting and Start of Code

print("Hello, welcome Jukebox Hero!") 

#   
#
#   Main Menu and Option Commands

mainMenu = False

while mainMenu == False:
    response = input("Please enter a command(press M for Menu): ")
    if response.lower() == "m":
        printMenu()

    # Insert command options--> load catalog, search catalog, analyse catalog, and print catalog
    elif response.lower() == "l":
        catalogFile = input("Please enter a file: ")
        songList = getListFromFile(catalogFile)
        print("Catalog uploaded!")
    elif response.lower() == "s":
        queryTerm = input("Please enter a search query: ")
        queryResults = findSongs(queryTerm,songList)
        for song in queryResults:
            printSong(song)
    elif response.lower() == "a":
        #  use a for loop and printSong() to print each song in songList
        printCatalogStats()
    elif response.lower() == "p":
        for song in songList:
            printSong(song)
    elif response.lower() == "q":
        mainMenu = True
        print("Thank you for accessing the Jukebox Hero! Please come again!")
