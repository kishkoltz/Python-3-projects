# D:\python3\app\python.exe thegame.py



import random
import time
import os
def clear():
    os.system('cls')
quit = 0
animals_finished = False
numbers_score = 0
menu = 0
myName = 0
#MAIN MENU
while quit == 0:
    if myName == 0:
        print ('Hello! What is your name?')
        myName = input ()
    clear()
    print ("")
    print ("      THE  GAME")
    print ("      MAIN MENU")
    print ("")
    print ("Hello %s, what would you like to do?" % myName)
    if numbers_score == 0:
        print ("1: Guess the number")
    else:
        print ("1: Guess the number | BEST TIME: %s" % numbers_score)
    if animals_finished == 0:
        print ("2: Name the animals")
    else:
        print ("2: Name the animals | FINISHED")
    print ("Q: Leave the game")
    print ("")
    menu = input()
    #while menu != ("1" or "2" or "Q"):
    while menu == 0:
        print ("Please type in \"1\", \"2\" or \"Q\".")
        menu = input ()
    else:
        if menu == ("1"):
            clear()
            guessesTaken = 0
            number = random.randint (1, 20)
            print ('Well, ' + myName +', \
I am thinking of a number between 1 and 20.')
            while guessesTaken < 3:
                print ('Take a guess.')
                guess = input ()
                while True:
                    try:
                        guess = int(guess)
                    except ValueError:
                        print ('Not an integer! Try again:')
                        guess = input ()
                    else:
                        break
                guess = int(guess)
                guessesTaken = guessesTaken + 1

                if guess < number:
                    print ('Your guess is too low.')
                if guess > number:
                    print ('Your guess is too high.')
                if guess == number:
                    break
            tip = random.randint (1, 4)
            low = number - tip
            high = number + (4 - tip)
            if low <= 0:
                low = 1
                high = 5
            if high >= 21:
                high = 20
                low = 16
            while guessesTaken < 6:
                if guess == number:
                    break
                print ('It is a number between %s and %s. Try again.'\
                 % (low, high))
                guess = input ()
                while True:
                    try:
                        guess = int(guess)
                    except ValueError:
                        print ('Not an integer! Try again:')
                        guess = input ()
                    else:
                        break
                guess = int(guess)

                guessesTaken = guessesTaken + 1

                if guess < number:
                    print ('Your guess is too low.')
                if guess > number:
                    print ('Your guess is too high.')
                if guess == number:
                    break

            if guess == number:
                guessesTaken = str (guessesTaken)
                if numbers_score == 0:
                    numbers_score = int(guessesTaken)
                if numbers_score >= 1:
                    if int(guessesTaken) < numbers_score:
                        numbers_score = int(guessesTaken)
                print ('Good job, %s! You guessed my number in %s guesses!'\
                 % (myName, guessesTaken))
                time.sleep (2)
            if guess != number:
                number = str (number)
                print ('Nope. The number I was thinking of was %s.' % number)
                time.sleep (2)
        if menu == "2":

            animal = 0
            cat = False
            dog = False
            frog = False
            dodo = False
            bird = False
            while animals_finished != True:
                if cat == True:
                    if dog == True:
                        if frog == True:
                            if bird == True:
                                if dodo == True:
                                    animals_finished = True
                while animal == 0:
                    animal = random.randint (1, 5)

                    if animal == 1:
                        if cat == 1:
                            animal = 0
                        if cat == 0:
                            animal = 'cat'
                            cat = True
                    if animal == 2:
                        if dog == 1:
                            animal = 0
                        if dog == 0:
                            animal = 'dog'
                            dog = True
                    if animal == 3:
                        if frog == 1:
                            animal = 0
                        if frog == 0:
                            animal = 'frog'
                            frog = True
                    if animal == 4:
                        if dodo == 1:
                            animal = 0
                        if dodo == 0:
                            animal = 'dodo'
                            dodo = True
                    if animal == 5:
                        if bird == 1:
                            animal = 0
                        if bird == 0:
                            animal = 'bird'
                            bird = True
                    if cat == True:
                        if dog == True:
                            if frog == True:
                                if bird == True:
                                    if dodo == True:
                                        animals_finished = True
                                        break
                    if animals_finished == True:
                        break
                clear()
                print ("")
                print ("Can you name this animal?")
                if animal == 'cat':
                    print("")
                    print("           |\      _,,,--,,_ ")
                    print("           /,`.-'`'   ._  \-;;,_ ")
                    print("          |,4-  ) )_   .;.(  `'-' ")
                    print("         '---''(_/._)-'(_\_)  ")
                    print ("")
                if animal == 'dog':
                    print ("")
                    print ("                        (\ ")
                    print ("                       (\_\_^__o ")
                    print ("                ___     `-'/ `_/ ")
                    print ("               '`--\______/  | ")
                    print ("          '        /         | ")
                    print ("      `    .  ' `-`/.------'\^-' ")
                    print ("")
                if animal == 'frog':
                    print ("")
                    print ("  .'_`--.___   __  ")
                    print (" ( 'o`   - .`.'_ )  ")
                    print ("  `-._      `_`./_  ")
                    print ("    '/\\    ( .'/ )  ")
                    print ("  ,__//`---'`-'_/  ")
                    print ("   /-'        '/  ")
                    print ("")
                if animal == 'dodo':
                    print ("")
                    print ("      ,---. ")
                    print ("    ,/     \__.'~\ ")
                    print ("    |        '  . `===---     ")
                    print ("    `|   ,     ,--' ")
                    print ("     `. /___,-' ")
                    print ("       |    \ ")
                    print ("       ,\_  ,`-= ")
                    print ("")
                if animal == 'bird':
                    print ("")
                    print ("     .--.  ")
                    print ("    /( @ >    ,-. ")
                    print ("   / ' .'--._/  / ")
                    print ("   :   ,    , .' ")
                    print ("   '. (___.'_/ ")
                    print ("    ((-((-' ")
                    print ("")
                print ("This animal is a ", end='')
                answer = input()
                while answer != animal:
                    print ("That's not a %s, try again!" % answer)
                    print ("This animal is a ", end='')
                    answer = input ()
                if answer == animal:
                    print ("That's right, this is a %s!" % animal)
                    animal = 0
                    time.sleep (1)
                if animals_finished == True:
                    break

        if menu == ("Q"):
            print ("")
            print ("Ok, bye!")
            time.sleep (1)
            clear()
            break
