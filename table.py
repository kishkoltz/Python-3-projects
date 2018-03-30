# D:\python3\app\python.exe table.py
def first():
    print ('haha')
    play()
def play():
    print ('poop')

def lastroom():
    print('whatevs')
def change ():
    global lastroom
    lastroom = play
life = 184

def damage(dmg):
    global life
    life = life - dmg
    print ("You've received %s damage." % str(dmg))
equipment = {}
def getSword():

    equipment['sword'] = 'blade'

def loseSword():
    del equipment['sword']
game = True
def get(item):
    equipment[item] = item

while game == True:
    lastroom()
    print ("You've got %s life." % str(life))
    print ("Equipment: %s" % equipment)
    damage(4)
    x = input()
    if x == '1':
        game = False
    print ("You've got %s life." % str(life))
    getSword()
    get('shit')
    if 'sword' in equipment:
        print ("You've got a blade.")
    if 'blade' in equipment:
        print ("You've got a sword.")
    print ("Equipment: %s" % (equipment.keys()))
    print (equipment['sword'])
    change()
    loseSword()
    print ("Equipment: %s" % equipment)
    if 'sword' in equipment:
        print ("You've got  blade.")
    x = input()
    print ("Now you'll add a piece of equipment: ")
    equipment[input('key: ')] = input('value: ')
    if x == '1':
        game = False
    lastroom()
    x = input()
    if x == '1':
        game = False
    #lastroom = first
    lastroom()
    x = input()
    if x == '1':
        game = False
