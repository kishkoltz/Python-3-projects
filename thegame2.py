# D:\python3\app\python.exe thegame2.py



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
            cat = ('''
           |\      _,,,--,,_
           /,`.-'`'   ._  \-;;,_
          |,4-  ) )_   .;.(  `'-'
         '---''(_/._)-'(_\_)
''')

            dog = ('''
                        (\\
                       (\_\_^__o
                ___     `-'/ `_/
               '`--\______/  |
          '        /         |
      `    .  ' `-`/.------'\^-'
''')

            frog = ('''
  .'_`--.___   __
 ( 'o`   - .`.'_ )
  `-._      `_`./_
    '/\\\\    ( .'/ )
  ,__//`---'`-'_/
   /-'        '/
''')

            kiwi = ('''
      ,---.
    ,/     \__.'~\\
    |        '  . `===---
    `|   ,     ,--'
     `. /___,-'
       |    \\
       ,\_  ,`-=
''')

            bird = ('''
     .--.
    /( @ >    ,-.
   / ' .'--._/  /
   :   ,    , .'
   '. (___.'_/
    ((-((-'
''')
            animal = {'cat':cat, 'dog':dog, 'frog':frog, 'kiwi':kiwi, 'bird':bird}

            while len(animal) >= 0:
                animal_of_choice = random.choice(list(animal.keys()))

                clear()
                print ("")
                print ("Animals Remaining: %s" % len(animal))
                print ("Can you name this animal?")
                if animal_of_choice == 'cat':
                    print (animal.pop('cat'))
                if animal_of_choice == 'dog':
                    print (animal.pop('dog'))
                if animal_of_choice == 'frog':
                    print (animal.pop('frog'))
                if animal_of_choice == 'kiwi':
                    print (animal.pop('kiwi'))
                if animal_of_choice == 'bird':
                    print (animal.pop('bird'))
                print ("This animal is a ", end='')
                answer = input()
                while answer != str(animal_of_choice):
                    if animal_of_choice == 'dog':
                        if answer == str('deer'):
                            print ("That's actually a basset hound, \
but I'll accept this answer as well.")
                            time.sleep (1.8)
                            break
                    print ("That's not a %s, try again!" % answer)
                    print ("This animal is a ", end='')
                    answer = input ()
                if answer == str(animal_of_choice):
                    print ("That's right, this is a %s!" % str(animal_of_choice))
                    time.sleep (1)
                if len(animal) == 0:
                    animals_finished = True
                    break

        if menu == ("Q"):
            print ("")
            print ("Ok, bye!")
            time.sleep (1)
            clear()
            break
