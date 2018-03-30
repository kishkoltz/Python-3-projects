# D:\python3\app\python.exe hangmanpro.py

import os
import time
import random
import getpass

def clear():
    os.system('cls')
clear()

print ('''
 +======#======+
 |      |      |
 |   X  |  II  |
 |     /D      |
 |     #       |     _,H    H,_     _,HHHHHHHH HHH,,,,_    _,HHHHHH,_  _,,,,HHH,,,,_    _,HHHHHHHH HHH,,,,_
 |  \\\\=M===/)  |     HHH    HHH     HHH    HHH HHH"""HH,   HHH    HHH _HH"""HHH"""HH,   HHH    HHH HHH"""HH,
 |     M  //   |     HHH    HHH     HHH    HHH HHH   HHH   HHH    H"  HHH   HHH   HHH   HHH    HHH HHH   HHH
 |     ==O=    |   _,HHH,,,,HHH,, __HHH____HHH HHH   HHH _,HHH ____   HHH   HHH   HHH __HHH____HHH HHH   HHH
 |    |    |   |   ""###""""###"  "########### ###   ### ""### ####,_ ###   ###   ### "########### ###   ###
 |   /|  _ |\\  |     ###    ###     ###    ### ###   ###   ###    ### ###   ###   ###   ###    ### ###   ###
 |   \\__/ \\_/  |     ###    ###     ###    ### ###   ###   ###    ### ###   ###   ###   ###    ### ###   ###
 |      Y'&\\   |     ###    #"      ###    #"   "#   #"    ########"   "#   ###   #"    ###    #"   "#   #"
 |      @.|.   |
 |      '""'   |
 |             |
 +-------------+
         ''')
time.sleep(2)
clear()

HANGMANPICS = ['''
 +======#======+
 |      |      |
 |   X  |  II  |
 |      #      |
 |      O      |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 +-------------+
 ''', '''
 +======#======+
 |      |      |
 |   X  |  II  |
 |     /D      |
 |     #       |
 |     M       |
 |     M       |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 +-------------+
 ''', '''
 +======#======+
 |      |      |
 |   X  |  II  |
 |     /D      |
 |     #       |
 |  \\\\=M===/)  |
 |     M  //   |
 |     ==O=    |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 |             |
 +-------------+
 ''', '''
 +======#======+
 |      |      |
 |   X  |  II  |
 |     /D      |
 |     #       |
 |  \\\\=M===/)  |
 |     M  //   |
 |     ==O=    |
 |    |    |   |
 |    |  _ |   |
 |   |__/ \\_|  |
 |             |
 |             |
 |             |
 |             |
 +-------------+
 ''', '''
 +======#======+
 |      |      |
 |   X  |  II  |
 |     /D      |
 |     #       |
 |  \\\\=M===/)  |
 |     M  //   |
 |     ==O=    |
 |    |    |   |
 |   /|  _ |   |
 |   \\__/ \\_|  |
 |             |
 |             |
 |             |
 |             |
 +-------------+
 ''', '''
 +======#======+
 |      |      |
 |   X  |  II  |
 |     /D      |
 |     #       |
 |  \\\\=M===/)  |
 |     M  //   |
 |     ==O=    |
 |    |    |   |
 |   /|  _ |\\  |
 |   \\__/ \\_/  |
 |             |
 |             |
 |             |
 |             |
 +-------------+
 ''', '''
 +======#======+
 |      |      |
 |   X  |  II  |
 |     /D      |
 |     #       |
 |  \\\\=M===/)  |
 |     M  //   |
 |     ==O=    |
 |    |    |   |
 |   /|  _ |\\  |
 |   \\__/ \\_/  |
 |      Y'&\\   |
 |      @.|.   |
 |      '""'   |
 |             |
 +-------------+
 ''']

gameOn = True
wordKey = ''
wordIndex = ''
secretWord = ''
secretKey = ''
missedLetters = ''
correctLetters = ''
player = {}
playerNumber = ''
multiKey = []
multiWord = []
multiPoints = {}
playersToGuess = {}
playersGuessed = {}
playerGuessing = ''
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def mainMenu():
    global gameOn
    while gameOn == True:
        clear()
        print ('''
+======#======+
|      |      |
|   X  |  II  |
|     /D      |         What would you like to do:
|     #       |
|  \\\\=M===/)  |
|     M  //   |         1) Play single player
|     ==O=    |
|    |    |   |
|   /|  _ |\\  |         2) Play multi player
|   \\__/ \\_/  |
|      Y'&\\   |
|      @.|.   |         Q) Quit
|      '""'   |
|             |
+-------------+
''')
        choice = input()
        while choice not in '12Q':
            choice = input('Please make a choice: ')
        if choice == 'Q':
            gameOn = False
            clear()
            print ("Thank you for playing!")
            time.sleep(2)
            break
        if choice == '1':
            singlePlayer()
            break
        if choice == '2':
            multiPlayer()
            break

def getRandomWord(wordDict):
    global wordKey
    global wordIndex
    # This function returns a random string from the passed dictionary of lists of strings, and the key also.
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))
    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print('Secret word category: ' + secretKey)
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print('(%s)' % letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    print()
    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print()
        print('Guess a letter: ', end= ' ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            if guess == secretWord:
                return guess
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def singlePlayer():
    global secretWord
    global secretKey
    global missedLetters
    global correctLetters
    global HANGMANPICS
    missedLetters = ''
    correctLetters = ''
    secretWord, secretKey = getRandomWord(words)
    gameIsDone = False

    while True:
        clear()
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)
        if guess == secretWord:
            clear()
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print()
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
        if guess in secretWord:
            correctLetters = correctLetters + guess

        # Check if the player has won
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                clear()
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print()
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
            if len(missedLetters) == len(HANGMANPICS) - 1:
                clear()
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print()
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            if playAgain():
                singlePlayer()
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord, secretKey = getRandomWord(words)
                break
            else:
                mainMenu()
                break
def multiPrint():
    count = 0
    while count != 5:
        print ('Count = ' + str(count))
        count = count +1
        input()

def multiPlayer():
    global playerNumber
    global player
    global secretKey
    global secretWord
    global multiPoints
    global playersToGuess
    playerNumber = input ('How many players will play the game? ')
    #while len(player) != int(playerNumber):
        #player.append(input('Please name the player number %s: ' % str(len(player)+1)))
    for x in range(1,int(playerNumber)+1):
        multiPoints[str(x)] = 0
    for x in range(1,int(playerNumber)+1):
        player[str(x)] = input("Please name the player number %s: " % str(len(player)+1))
    for x in range(1,int(playerNumber)+1):
        secretKey = getpass.getpass("%s, please provide the category of your secret word: " % player[str(x)])
        secretWord = getpass.getpass("%s, please provide your secret word: " % player[str(x)]).lower()
        for s in range(1,int(playerNumber)+1):
	           playersToGuess[s] = s
        del playersToGuess[x]
        multiPrint()
        multiGame(x)

def playerChoice():
    global playerGuessing
    global playersToGuess
    global playersGuessed
    if len(playersToGuess) > 0 :
        playerGuessing = random.choice(list(playersToGuess.keys()))
        playersGuessed[playerGuessing] = playerGuessing
        del playersToGuess[playerGuessing]
    else:
        playersToGuess = playersGuessed
        playersGuessed = {}
        playerGuessing = random.choice(list(playersToGuess.keys()))
        playersGuessed[playerGuessing] = playerGuessing
        del playersToGuess[playerGuessing]

def multiGame(x):
    global missedLetters
    global correctLetters
    global HANGMANPICS
    missedLetters = ''
    correctLetters = ''
    gameIsDone = False

    while True:
        clear()
        playerChoice()
        print(("%s's turn" % player[str(playerGuessing)]).center(120))
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)
        if guess == secretWord:
            clear()
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print()
            print('Yes, ' + player[str(playerGuessing)] + '! The secret word is "' + secretWord + '"! You have won!')
            #multiPoints[playerGuessing] = multiPoints.values[playerGuessing] + 1
            gameIsDone = True
            break
        if guess in secretWord:
            correctLetters = correctLetters + guess

            # Check if the player has won
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                clear()
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print()
                print('Yes, ' + player[str(playerGuessing)] + '! The secret word is "' + secretWord + '"! You have won!')
                multiPoints[int(playerGuessing)] = str(int(multiPoints.values[playerGuessing]) + 1)
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            clear()
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print()
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            multiPoints[x+1] = multiPoints.values[x] + 1
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
#        if gameIsDone:
#            if playAgain():
#                singlePlayer()
#                missedLetters = ''
#                correctLetters = ''
#                gameIsDone = False
#                secretWord, secretKey = getRandomWord(words)
#                break
#            else:
#                mainMenu()
        #break

mainMenu()
