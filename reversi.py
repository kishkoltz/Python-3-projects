# H:\python3\app\python.exe reversi.py

import random
import sys


def drawBoard(board):
    HLINE = ' +---+---+---+---+---+---+---+---+'
    VLINE = ' |   |   |   |   |   |   |   |   |'

    print('   1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        print(VLINE)
        print(y+1, end='')
        for x in range(8):
            #prints the contents of each line and each column separated by lines
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)

def resetBoard(board):
    #substitutes all fields with blanks
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
    #places the first four pieces on their fields
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

def getNewBoard():
    #resets the contents of the board to none
    board = []
    #appends the list with 64 blanks
    for i in range(8):
        board.append([' ']*8)
    return board

def isValidMove(board, tile, xstart, ystart):
    #checks if the field is empty and within the board limits
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    #assigns the specific field with a tile
    board[xstart][ystart] = tile
    #identifies the other tile
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    #probing fields around the selected field
    for xdirection, ydirection in [[0, 1], [1, 1], [1,0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        #continues if the field is occupied by another tile AND is within the board's limits
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            #goes in the confirmed direction until the other tiles are on the way
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                #the move is invalid if doesn't end with the player's tile
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            #confirms the move that ends with the player's tile
            if board[x][y] == tile:
                #identifies the tiles to flip
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    #clears the queried field
    board[xstart][ystart] = ' '
    #if there are no tiles to flip the move is invalid
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip

def isOnBoard(x, y):
    #checks if the field is on board
    return x >= 0 and x <= 7 and y >= 0 and y <= 7

def getBoardWithValidMoves(board, tile):
    #gets a duplicate of a board
    dupeBoard = getBoardCopy(board)
    #marks the valid moves with a dot
    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '.'
    return dupeBoard

def getValidMoves (board, tile):
    #resets the list of valid moves to none
    validMoves = []
    #checks each move and appends it if valid
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    #returns a list of valid moves
    return validMoves

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    #searches the board for tiles and appends the score accordingly
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enterPlayerTile():
    #resets the tile assignemnt
    tile = ''
    #lets the player choose the tile
    while not (tile == 'X' or tile == 'O'):
        print ('Do you want to be X or O?')
        tile = input().upper()
    if tile == 'X':
        #returns the player tile and the computer tile
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print ('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, tile, xstart, ystart):
    #checks if the move is valid
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False
    #places the tile on the board
    board[xstart][ystart] = tile
    #flips the opponent's tiles
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    #gets a board copy
    dupeBoard = getNewBoard()

    #places all the tiles on the board
    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard

def isOnCorner(x, y):
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 0) or (x == 7 and y == 7)

def getPlayerMove(board, playerTile):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'. split()
    while True:
        print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')
        move = input().lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        #checks if the move consists of two digits from 1 to 8
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            #subtracts the sum so that the location is in sync with the database
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            #notifies the player if the move is invalid and requests a new one
            if isValidMove(board, playerTile, x, y) == False:
                continue
            #breaks the loop if the move is valid and jumps to return the x&y
            else:
                break
        else:
            print('That is not a valid move. Type the x digit (1-8), then the y digit (1-8).')
            print('For example, 81 will be the top-right corner.')
    return [x, y]

def getComputerMove(board, computerTile):
    #gets a list of valid moves
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)
    #puts priority on corner moves
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]
    bestScore = -1
    #checks the score for each move and chooses the best scoring one
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def showPoints(playerTile, computerTile):
    #gest the score and prints it
    scores = getScoreOfBoard(mainBoard)
    print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))

print('Welcome to Reversi!')

while True:
    mainBoard = getNewBoard()
    drawBoard(mainBoard)
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    while True:
        if turn == 'player':
            #if hints are enabled the board is drawn with possible moves
            if showHints:
                validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
                drawBoard(validMovesBoard)
            else:
                drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            move = getPlayerMove(mainBoard, playerTile)
            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            elif move == 'hints':
                showHints = not showHints
                continue
            else:
                makeMove(mainBoard, playerTile, move[0], move[1])

            #finishes the playthrough when no moves are available
            if getValidMoves(mainBoard, computerTile) == []:
                break
            else:
                turn = 'computer'
        #computer's turn
        else:
            drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            input('Press Enter to see the Computer\'s move.')
            x, y = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, x, y)

            if getValidMoves(mainBoard, playerTile) == []:
                break
            else:
                turn = 'player'
    #shows the results
    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
    else:
        print('The game was a tie!')

    if not playAgain():
        break
