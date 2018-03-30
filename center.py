# D:\python3\app\python.exe center.py
answer = ''
true = True
globalne = True

def room():
    global globalne
    globalne = False
    print (globalne)

while true == True:
    print ('Type someting:', end = '')
    answer = input()
    center = (120 - len(answer))/2
    spaces = " " * int(center)
    print ('The number of characters = %s.' % (len(answer)))
    print ('The number of spaces before = %s.' % center)
    if answer == 'quit':
        true = False
    else:
        print (spaces + answer)
        print (answer.center(120))
        print (true)

        print ("Globalne is %s." % str(globalne))
        room()
        print ()
        print ("Globalne is %s." % str(globalne))
