# D:\python3\app\python.exe hangman.py
import os
import time
import random

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
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

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



missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    clear()
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

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
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            clear()
            break
