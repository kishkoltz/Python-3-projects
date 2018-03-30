# D:\python3\app\python.exe bagels.py


import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum(NUM_DIGITS):
    #returns a string of unique random digits that is NUM_DIGITS long
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    #returns a string with the pico, fermi, bagels clues to the user
    if guess == secretNum:
        return "You got it!"
    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'

    clue.sort()
    return ' '.join(clue)

def isOnlyDigits(num):
    #returns True if num is a string made up only of digits. Otherwise returns False
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

def playAgain():
    #this function returns True if player wants to play again, otherwise returns False
    print ("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

print("I am thinking of a %s-digit number. Try to guess what it is." % (NUM_DIGITS))
print("Here are some clues:")
print("When I say:      That means:")
print("     Pico        One digit is correct but in the wrong position")
print("     Fermi       One digit is correct and in the right position")
print("     Bagels      No digit is correct.")

while True:
    secretNum = getSecretNum(NUM_DIGITS)
    print("I have thoiught up a number. You have % guesses to get it." % (MAX_GUESS))

    numGuesses = 1
    while numGuesses <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print ("Guess #%s: " % (numGuesses))
            guess = input()

        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1

        if guess == secretNum:
            break
        if numGuesses > MAX_GUESS:
            print ("You ran out of guesses. The answer was %s" % (secretNum))

    if not playAgain():
        break
