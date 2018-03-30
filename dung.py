gameOn = True
level = ''
trap = ''

def dungeon(level):
    global gameOn
    if level == 1:
        print ('level')
    if level == 2:
        print ('a trap!')
        gameOn = False

while gameOn == True:
    choice = input('Choose: ')
    if choice == '1':
        dungeon(1)
    if choice == '2':
        dungeon(2)
