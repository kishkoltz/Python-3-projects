import time
from threading import Thread
slow = ''
answer = None

def check():
    global slow
    if answer != None:
        return
    time.sleep(1)
    print ()
    if answer != None:
        return
    print ("3... ")
    time.sleep(1)
    if answer != None:
        return
    print ("2... ")
    time.sleep(1)
    if answer != None:
        return
    print ("1... ")
    time.sleep(1)
    if answer != None:
        return
    slow = True
    if slow == True:
        print ("C'mon, choose already:")


Thread(target = check).start()
answer = input("Choose:\n1\n2\nYour answer: ")
if answer == '1':
    if slow == True:
        print ('You chose 1, but you were too slow.')
    else:
        print ("You chose 1.")
if answer == '2':
    if slow == True:
        print ('You chose 2, but you were too slow.')
    else:
        print ("You chose 2.")
