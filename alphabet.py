# D:\python3\app\python.exe alphabet.py
import random
import os
def clear():
    os.system('cls')
clear()
alphabet = {}
for x in 'abcdefghijklmnoprstuvwxyz':
    alphabet [x] = x
print (alphabet)
on = True

while on == True:
    clear()
    print ()
    letter = random.choice(list(alphabet.keys()))
    del alphabet[letter]
    print (letter.center(120))
    choice = input()
    if choice == 'q':
        on == False
        break
