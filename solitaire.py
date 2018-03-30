# D:\python3\app\python.exe solitaire.py
import random
import time
import os
def clear():
    os.system('cls')

playLive = True
gameFinished = None
deck = []

A = []
B = []
C = []
D = []
E = []
F = []
G = []
rows = [A, B, C, D, E, F, G]

Ah = []
Bh = []
Ch = []
Dh = []
Eh = []
Fh = []
Gh = []
hiddenRows = [Ah, Bh, Ch, Dh, Eh, Fh, Gh]

cardValue = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cardColor = ['H', 'D', 'S', 'C']
hearts = []
diamonds = []
spades = []
clubs = []
piles = [hearts, diamonds, spades, clubs]

rowName = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def deal():
    #fills the deck with cards
    for c in cardColor:
        for v in cardValue:
            deck.append(v + c)
    #shuffles the deck
    random.shuffle(deck)
    #fills the rows with cards
    for r in range(7):
        for c in range(7-r):
            rows[r].append(deck[0])
            deck.remove(deck[0])
    #turns the dealt cards face down
    for h in range(7):
        for c in range(6 - h):
            hiddenRows[h].append('[ ]')
def discardPiles():
    #prints discard piles for separate colours
    if len(hearts) > 0:
        print ('(H)EARTS: %s      ' % hearts[len(hearts) - 1], end = '')
    else:
        print ('(H)EARTS: empty   ', end = '')
    if len(diamonds) > 0:
        print ('(D)IAMONDS: %s    ' % diamonds[len(diamonds) - 1], end = '')
    else:
        print ('(D)IAMONDS: empty ', end = '')
    if len(spades) > 0:
        print ('(S)PADES: %s      ' % spades[len(spades) - 1], end = '')
    else:
        print ('(S)PADES: empty   ', end = '')
    if len(clubs) > 0:
        print ('(C)LUBS: %s       ' % clubs[len(clubs) - 1])
    else:
        print ('(C)LUBS: empty    ')
def printDeck():
    clear()
    # on the rows below the information from rows (12-18) and hiddenRows(21-28)
    # will be compiled.
    fA = []
    fB = []
    fC = []
    fD = []
    fE = []
    fF = []
    fG = []
    falseRows = [fA, fB, fC, fD, fE, fF, fG]
    print ('')
    if len(deck) >= 3:
        print ('Draw pile: [%s] %s %s   ' % (deck[0], deck[1], deck[2]), end = '')
    if len(deck) == 2:
        print ('Draw pile: [%s] %s   ' % (deck[0], deck[1]), end = '')
    if len(deck) == 1:
        print ('Draw pile: [%s]   ' % deck[0], end = '')
    print("Draw pile total: %s  " % len(deck), end = '')
    discardPiles()
    print ('')
    for r in range(7):
        for c in range(len(rows[r])):
            falseRows[r].append(rows[r][c])
    for r in range(7):
        for c in range(len(hiddenRows[r])):
            falseRows[r][c] = '[ ]'
    for r in range(7):
        print ('%s: ' % (rowName[r]), end = '')
        for c in range(len(falseRows[r])):
            if len(falseRows[r][c]) == 2:
                print ('%s  ' % falseRows[r][c], end = '')
            else:
                print ('%s ' % falseRows[r][c], end = '')
        print ('')
        print ('')
def chooseMove():
    global playLive
    print('What would you like to do next:')
    print('(M)OVE a card:')
    print('(D)ISCARD a card')
    print('(T)AKE the first card from a draw pile')
    print('(S)HOW next three cards in a draw pile')
    print('(Q)UIT')
    print('(F)LUSH')
    choice = input().upper()
    if choice == 'M':
        moveCard(input('Which card would you like to move? ').upper(),input('Where would you like to move it? Row: ').upper())
    if choice == 'D':
        discardCard(input('Which card would you like to discard? ').upper())
    if choice == 'T':
        drawPileAction('T')
    if choice == 'S':
        drawPileAction('S')
    if choice == 'F':
        for r in range(7):
            rows[r] = []
            hiddenRows[r] = []
    if choice == 'Q':
        print('Very Well. Goodbye!')
        playLive = False
def moveCard(choice,destination):
    moveValid = None
    for v in range(len(cardValue)):
        if cardValue[v] in choice:
            print ('the card has correct value')
            for c in range(4):
                if cardColor[c] in choice:
                    print ('the card has correct color')
                    for r in range(7):
                        if rowName[r] in destination:
                            print('selected row is on the board')
                            moveValid = True
    cardInfo = [] #row, number, value, color
    destinationInfo = []
    moveLegit = None
    #getting card's info
    if moveValid == True:
        for r in range(7):
            for c in range(len(rows[r])):
                if choice == rows[r][c]:
                    cardInfo.append(r)
                    cardInfo.append(c)
        for v in range(13):
            if cardValue[v] in choice:
                cardInfo.append(v)
        if 'H' in choice:
            cardInfo.append(0)
        elif 'D' in choice:
            cardInfo.append(0)
        else:
            cardInfo.append(1)
        #getting destination's info
        for d in range(7):
            if destination in rowName[d]:
                destinationInfo.append(d)
                moveLegit = True
                if len(rows[d]) > 0:
                    destinationInfo.append(len(rows[d])-1)
                    for v in range(13):
                        if cardValue[v] in rows[d][len(rows[d])-1]:
                            destinationInfo.append(v)
                    if 'H' in rows[d][len(rows[d])-1]:
                        destinationInfo.append(0)
                    elif 'D' in rows[d][len(rows[d])-1]:
                        destinationInfo.append(0)
                    else:
                        destinationInfo.append(1)
                else:
                    destinationInfo.append('E')

        print ("Card's Info: %s" % cardInfo)
        print ("Destination's Info: %s" % destinationInfo)
        #checking if the move is valid
        if moveLegit == True:
            if destinationInfo[1] != 'E':
                print ("the chosen row is not empty.")
                if cardInfo[2] > 0:
                    print("The card is not an ace.")
                    if cardInfo[2] == (destinationInfo[2]-1):
                        print ('The card is of a lower value. Proceeding.')
                        if cardInfo[3] != destinationInfo[3]:
                            print ('The card is of an opposite color. Proceeding.')
                            if len(hiddenRows[cardInfo[0]]) < (cardInfo[1] +1):
                                print("the card is face up")
                #All requirements matched, move valid
                                for cards in range(len(rows[cardInfo[0]])-cardInfo[1]):
                                    print("%s cards will be moved." % (len(rows[cardInfo[0]])-cardInfo[1]))
                #adding the stack to the new row
                                    rows[destinationInfo[0]].append(rows[cardInfo[0]][cardInfo[1]])
                                    print ("adding the stack to the new row")
                #removing the stack from the old row
                                    rows[cardInfo[0]].remove(rows[cardInfo[0]][cardInfo[1]])
                #rows[cardInfo[0]].remove(rows[[cardInfo[0]][cardInfo[1]]])
                                    print("removing the stack from the old row")
                                print ("Proceeding to turn cards face-up")
                                if len(hiddenRows[cardInfo[0]]) > 0:
                                    print("There are cards to be turned face up.")
                                    for hidden in range(len(hiddenRows[cardInfo[0]])-cardInfo[1]+1):
                                        print ("%s cards to be turned face-up" % str(len(rows[cardInfo[0]])-cardInfo[1]))
                                        hiddenRows[cardInfo[0]].remove(hiddenRows[cardInfo[0]][cardInfo[1]-1])
                                        print("turning cards face-up")
                else:
                    if cardInfo[2] == 0:
                        print("The card is an ace. Discarding the card instead.")
                        discardCard(choice)
            elif destinationInfo[1] == 'E':
                print("The row is empty.")
                if cardInfo[2] > 0:
                    print("The card is not an ace.")
                    if cardInfo[2] == 12:
                        print("The selected card is a king.")
                        for cards in range(len(rows[cardInfo[0]])-cardInfo[1]):
                            print("%s cards will be moved." % (len(rows[cardInfo[0]])-cardInfo[1]))
            #adding the stack to the new row
                            rows[destinationInfo[0]].append(rows[cardInfo[0]][cardInfo[1]])
                            print ("adding the stack to the new row")
            #removing the stack from the old row
                            rows[cardInfo[0]].remove(rows[cardInfo[0]][cardInfo[1]])
            #rows[cardInfo[0]].remove(rows[[cardInfo[0]][cardInfo[1]]])
                            print("removing the stack from the old row")
                        print ("Proceeding to turn cards face-up")
                        if len(hiddenRows[cardInfo[0]]) > 0:
                            print("There are cards to be turned face up.")
                            for hidden in range(len(hiddenRows[cardInfo[0]])-cardInfo[1]+1):
                                print ("%s cards to be turned face-up" % str(len(rows[cardInfo[0]])-cardInfo[1]))
                                hiddenRows[cardInfo[0]].remove(hiddenRows[cardInfo[0]][cardInfo[1]-1])
                                print("turning cards face-up")
                else:
                    if cardInfo[2] == 0:
                        print("The card is an ace. Discarding the card instead.")
                        discardCard(choice)
def discardCard(choice):
    print('Card to discard: %s' % choice)
    moveValid = None
    for v in range(13):
        #print('checking the card value')
        if cardValue[v] in choice:
            #print ('the card has correct value. checking its color')
            for c in range(4):
                if cardColor[c] in choice:
                    #print ('the card has correct color')
                    for r in range(7):
                        for c in range(len(rows[r])):
                            if choice == rows[r][c]:
                                moveValid = True
    cardInfo = [] #row, number, value, color
    destinationInfo = [] #always a last one, so number = value
    #getting card's info
    if moveValid == True:
        #getting card's info
        for r in range(7):
            for c in range(len(rows[r])):
                if choice == rows[r][c]:
                    cardInfo.append(r)
                    cardInfo.append(c)
        for v in range(13):
            if cardValue[v] in choice:
                cardInfo.append(v)
        for p in range(4):
            if cardColor[p] in choice:
                cardInfo.append(p)
        print ("Card's Info: %s" % cardInfo)
        #print ("Destination's Info: %s" % destinationInfo)
        #separate rules for aces in order to avoid IndexErrors
        if cardInfo[2] == 0:
            print ('The selected card is an ace.')
            if len(piles[cardInfo[3]]) == 0:
                print ("The discard pile is empty")
                if cardInfo[1] == (len(rows[cardInfo[0]])-1):
                    print ('The card is the last one in its row. Proceeding.')
                    if len(hiddenRows[cardInfo[0]]) < (cardInfo[1] +1):
                        print("the card is face up")
                        for cards in range(len(rows[cardInfo[0]])-cardInfo[1]):
                            print("%s cards will be moved." % (len(rows[cardInfo[0]])-cardInfo[1]))
                            #adding the stack to the new row
                            piles[cardInfo[3]].append(rows[cardInfo[0]][cardInfo[1]])
                            print ("adding the stack to the pile")
                            #removing the stack from the old row
                            rows[cardInfo[0]].remove(rows[cardInfo[0]][cardInfo[1]])
                            print("removing the stack from the old row")
                        print ("Proceeding to turn cards face-up")
                        if len(hiddenRows[cardInfo[0]]) > 0:
                            print("There are cards to be turned face up.")
                            for hidden in range(len(hiddenRows[cardInfo[0]])-cardInfo[1]+1):
                                print ("%s cards to be turned face-up" % str(len(rows[cardInfo[0]])-cardInfo[1]))
                                hiddenRows[cardInfo[0]].remove(hiddenRows[cardInfo[0]][cardInfo[1]-1])
                                print("turning cards face-up")

        #checking if the move is valid
    if moveValid == True:
        if cardInfo[2] > 0:
            print ("The selected card is not an ace.")
            if cardInfo[2] == (len(piles[cardInfo[3]])):
                print ('The card is of a higher value. Proceeding.')
                if cardInfo[1] == (len(rows[cardInfo[0]])-1):
                    print ('The card is the last one in its row. Proceeding.')
                    if len(hiddenRows[cardInfo[0]]) < (cardInfo[1] +1):
                        print("the card is face up")
                        #All requirements matched, move valid
                        for cards in range(len(rows[cardInfo[0]])-cardInfo[1]):
                            print("%s cards will be moved." % (len(rows[cardInfo[0]])-cardInfo[1]))
                            #adding the stack to the new row
                            piles[cardInfo[3]].append(rows[cardInfo[0]][cardInfo[1]])
                            print ("adding the stack to the pile")
                            #removing the stack from the old row
                            rows[cardInfo[0]].remove(rows[cardInfo[0]][cardInfo[1]])
                            print("removing the stack from the old row")
                        print ("Proceeding to turn cards face-up")
                        if len(hiddenRows[cardInfo[0]]) > 0:
                            for hidden in range(len(hiddenRows[cardInfo[0]])-cardInfo[1]+1):
                                print ("%s cards to be turned face-up" % str(len(rows[cardInfo[0]])-cardInfo[1]))
                                hiddenRows[cardInfo[0]].remove(hiddenRows[cardInfo[0]][cardInfo[1]-1])
                                print("turning cards face-up")
def drawPileAction(choice):
    if choice == 'S':
        for r in range(3):
            deck.append(deck[0])
            deck.remove(deck[0])
    drawCard = [] #value, color
    destinationInfo = [] #row, value, color
    option = []
    if choice == 'T':
        for v in range(13):
            if cardValue[v] in deck[0]:
                drawCard.append(v)
                #print('card value checked: %s' % drawCard[0])
                for x in range(4):
                    if cardColor[x] in deck[0]:
                        drawCard.append(x)
                        #print('card color checked: %s' % drawCard[1])
                    #print("fail")
            else:
                None
                #print("Fail")
        #print("checking stuff")
        if drawCard[0] == 0:
            print('326.The card is an ace and can be put on the discard pile')
            option.append(0)
        if drawCard[0] > 0:
            print("Value more than 0")
            if drawCard[0] == len(piles[drawCard[1]]):
                print('331.The card can be put on the discard pile')
                option.append(0)
            else:
                print('334.The card can be placed on board')
                option.append(1)
        if option[0] == 0:
            print('337.The card can be put on the discard pile.')
            piles[drawCard[1]].append(deck[0])
            deck.remove(deck[0])
        if option[0] == 1:
            destination = input('341. Which row should the card be placed on?').upper()
            goodToGo = None
            for r in range(7):
                if rowName[r] in destination:
                    destinationInfo.append(r) #appends row value
                    goodToGo = True
            if goodToGo == True:
                print('346. the chosen row is %s.' % rowName[destinationInfo[0]])
                if len(rows[destinationInfo[0]]) > 0:
                    for v in range(13):
                        if cardValue[v] in rows[destinationInfo[0]][len(rows[destinationInfo[0]])-1]:
                            print ('350. destination card value is %s.' % cardValue[v])
                            destinationInfo.append(v) #appends the card value
                            if 'H' in rows[destinationInfo[0]][len(rows[destinationInfo[0]])-1]:
                                print('353. the card on the destination row is red')
                                destinationInfo.append(0)
                            elif 'D' in rows[destinationInfo[0]][len(rows[destinationInfo[0]])-1]:
                                print('356. the card on the destination row is red')
                                destinationInfo.append(0)
                            else:
                                print('359. the card on the destination row is black')
                                destinationInfo.append(1)
                    if drawCard[0] == (destinationInfo[1]-1):
                        print('362. The pile card is of a lower value than the destination')
                        if drawCard[1] == 0:
                            drawCard[1] = 0
                        if drawCard[1] == 1:
                            drawCard[1] = 0
                        if drawCard[1] == 2:
                            drawCard[1] = 1
                        if drawCard[1] == 3:
                            drawCard[1] = 1
                        print ('Draw card info %s' % drawCard)
                        print('destination card info %s' % destinationInfo)
                        if drawCard[1] != destinationInfo[2]:
                            print('364. The pile card is of a different color')
                            rows[destinationInfo[0]].append(deck[0])
                            deck.remove(deck[0])
                        else:
                            print ("cards are of the same color")
                if len(rows[destinationInfo[0]]) == 0:
                    print('the selected row is empty.')
                    if drawCard[0] == 12:
                        print('the draw card is a king.')
                        rows[destinationInfo[0]].append(deck[0])
                        deck.remove(deck[0])
def gameItself():
    global playLive
    global gameFinished
    while playLive == True:
        deal()
        while playLive == True:
            printDeck()
            chooseMove()
            #if playLive == False:
            #    break
            if len(rows[0]) == 0:
                if len(rows[1]) == 0:
                    if len(rows[2]) == 0:
                        if len(rows[3]) == 0:
                            if len(rows[4]) == 0:
                                if len(rows[5]) == 0:
                                    if len(rows[6]) == 0:
                                        playAgain()
                                        break
def playAgain():
    global playLive
    printDeck()
    choice = input('Well done! Play again? Y/N: ').upper()
    while choice not in 'YN':
        choice = input('Please make a choice. Y/N: ').upper()
    if 'Y' in choice:
        #removes all remaining cards in the deck
        for r in range(len(deck)):
            deck.remove(deck[0])
        #removes cards from rows and indicators for face-down cards
        for p in range(7):
            rows[p] = []
            hiddenRows[p] = []
        #removes cards from the discard piles
        for p in range(4):
            for c in range(len(piles[p])):
                piles[p].remove(piles[p][0])

    if 'N' in choice:
        playLive = False


gameItself()
