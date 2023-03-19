# Game Tic-Tac-Toe
# Author: Bruno Beuttler
# Jugendgruppe FabLab Nuernberger Land
# Version Release 01.2

# imports
import random

# variables
players = "2"
playWanted = True
activePlayer = 1
activatedFields = 0
fields = {
    "2": "__",
    "3": "__",
    "4": "__",
    "5": "__",
    "6": "__",
    "7": "__",
    "1": "__",
    "8": "__",
    "9": "__",
}
stemps = [
    "A",
    "B"
]
players = input("How many players? 1 or 2? ")

stemps[0] = input('Player 1, please enter your stemp, for example "X": ')
if players == "2":
    stemps[1] = input('Player 2, please enter your stemp, for example "O": ')
else:
    stemps[1] = input('please enter the stemp for the computer, for example "O": ')

# shows the field at the beginning of the game

print('1_|2_|3_')
print('4_|5_|6_')
print('7 |8 |9 ')
print()

# returns "True" if someone won

def checkWinner():
    if fields["1"] == stemps[0] + "_" and fields["2"] == stemps[0] + "_" and fields["3"] == stemps[0] + "_":
        print('Player 1 won')
        return True
    
    if fields["1"] == stemps[1] + "_" and fields["2"] == stemps[1] + "_" and fields["3"] == stemps[1] + "_":
        print('Player 2 won')
        return True
    
    if fields["4"] == stemps[0] + "_" and fields["5"] == stemps[0] + "_" and fields["6"] == stemps[0] + "_":
        print('Player 1 won')
        return True
    
    if fields["4"] == stemps[1] + "_" and fields["5"] == stemps[1] + "_" and fields["6"] == stemps[1] + "_":
        print('Player 2 won')
        return True
    
    if fields["7"] == stemps[0] + "_" and fields["8"] == stemps[0] + "_" and fields["9"] == stemps[0] + "_":
        print('Player 1 won')
        return True
    
    if fields["7"] == stemps[1] + "_" and fields["8"] == stemps[1] + "_" and fields["9"] == stemps[1] + "_":
        print('Player 2 won')
        return True
    
    if fields["1"] == stemps[0] + "_" and fields["4"] == stemps[0] + "_" and fields["7"] == stemps[0] + "_":
        print('Player 1 won')
        return True
    
    if fields["1"] == stemps[1] + "_" and fields["4"] == stemps[1] + "_" and fields["7"] == stemps[1] + "_":
        print('Player 2 won')
        return True
    
    if fields["2"] == stemps[0] + "_" and fields["5"] == stemps[0] + "_" and fields["8"] == stemps[0] + "_":
        print('Player 1 won')
        return True
    
    if fields["2"] == stemps[1] + "_" and fields["5"] == stemps[1] + "_" and fields["8"] == stemps[1] + "_":
        print('Player 2 won')
        return True
    
    if fields["3"] == stemps[0] + "_" and fields["6"] == stemps[0] + "_" and fields["9"] == stemps[0] + "_":
        print('Player 1 won')
        return True
    
    if fields["3"] == stemps[1] + "_" and fields["6"] == stemps[1] + "_" and fields["9"] == stemps[1] + "_":
        print('Player 2 won')
        return True
    
    if fields["1"] == stemps[0] + "_" and fields["5"] == stemps[0] + "_" and fields["9"] == stemps[0] + "_":
        print('Player 1 won')
        return True
    
    if fields["1"] == stemps[1] + "_" and fields["5"] == stemps[1] + "_" and fields["9"] == stemps[1] + "_":
        print('Player 2 won')
        return True
    
    if fields["3"] == stemps[0] + "_" and fields["5"] == stemps[0] + "_" and fields["7"] == stemps[0] + "_":
        print('Player 1 won')
        return True
    
    if fields["3"] == stemps[1] + "_" and fields["5"] == stemps[1] + "_" and fields["7"] == stemps[1] + "_":
        print('Player 2 won')
        return True
    
# main function to run the game
    
while 1:
    if playWanted == True:
        if checkWinner() == True:
            break
        
        if activatedFields == 9:
            print('Game over, no player won')
            print(fields["1"] + '|' + fields["2"] + '|' + fields["3"])
            print(fields["4"] + '|' + fields["5"] + '|' + fields["6"])
            print(fields["7"] + '|' + fields["8"] + '|' + fields["9"])
            break
        
        playWanted = False
        
        if players == "1":
            if activePlayer == 1:
                print('Player ' + stemps[activePlayer - 1])
                newField = input('Where do you want to set? ')
                if fields[newField] == "__":
                    fields[newField] = stemps[activePlayer - 1] + "_"
            
                    print(fields["1"] + '|' + fields["2"] + '|' + fields["3"])
                    print(fields["4"] + '|' + fields["5"] + '|' + fields["6"])
                    print(fields["7"] + '|' + fields["8"] + '|' + fields["9"])
                    print()
                    
                    if activePlayer == 1:
                        activePlayer = 2
                    else:
                        activePlayer = 1
                    
                    activatedFields += 1    
                    playWanted = True
            else:
                while 1:
                    randomLetter = random.choice("123456789")
                    print(randomLetter)
                    
                    if fields[randomLetter] == "__":
                        fields[randomLetter] = stemps[1] + "_"
                        print(fields["1"] + '|' + fields["2"] + '|' + fields["3"])
                        print(fields["4"] + '|' + fields["5"] + '|' + fields["6"])
                        print(fields["7"] + '|' + fields["8"] + '|' + fields["9"])
                        print()
                        activePlayer = 1
                        activatedFields += 1
                        playWanted = True
                        break
            
        else:
            print('Player ' + stemps[activePlayer - 1])
            
            newField = input('Where do you want to set? ')
            if fields[newField] == "__":
                fields[newField] = stemps[activePlayer - 1] + "_"
        
                print(fields["1"] + '|' + fields["2"] + '|' + fields["3"])
                print(fields["4"] + '|' + fields["5"] + '|' + fields["6"])
                print(fields["7"] + '|' + fields["8"] + '|' + fields["9"])
                print()
                
                if activePlayer == 1:
                    activePlayer = 2
                else:
                    activePlayer = 1
                
                activatedFields += 1    
                playWanted = True
                
    else:
        print()
        playWanted = True
        