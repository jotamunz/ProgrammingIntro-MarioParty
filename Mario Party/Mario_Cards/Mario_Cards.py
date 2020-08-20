import pygame
import random
import sys
import math

#====================================================================
#                           GLOBALS
#====================================================================

white = (255,255,255)
black = (0,0,0)

block = pygame.image.load("Mario_Cards/Cards/back.png")
a1 = pygame.image.load("Mario_Cards/Cards/A1.png")
b1 = pygame.image.load("Mario_Cards/Cards/B1.png")
c1 = pygame.image.load("Mario_Cards/Cards/C1.png")
d1 = pygame.image.load("Mario_Cards/Cards/D1.png")
a2 = pygame.image.load("Mario_Cards/Cards/A2.png")
b2 = pygame.image.load("Mario_Cards/Cards/B2.png")
c2 = pygame.image.load("Mario_Cards/Cards/C2.png")
d2 = pygame.image.load("Mario_Cards/Cards/D2.png")
a3 = pygame.image.load("Mario_Cards/Cards/A3.png")
b3 = pygame.image.load("Mario_Cards/Cards/B3.png")
c3 = pygame.image.load("Mario_Cards/Cards/C3.png")
d3 = pygame.image.load("Mario_Cards/Cards/D3.png")
a4 = pygame.image.load("Mario_Cards/Cards/A4.png")
b4 = pygame.image.load("Mario_Cards/Cards/B4.png")
c4 = pygame.image.load("Mario_Cards/Cards/C4.png")
d4 = pygame.image.load("Mario_Cards/Cards/D4.png")
a5 = pygame.image.load("Mario_Cards/Cards/A5.png")
b5 = pygame.image.load("Mario_Cards/Cards/B5.png")
c5 = pygame.image.load("Mario_Cards/Cards/C5.png")
d5 = pygame.image.load("Mario_Cards/Cards/D5.png")
a6 = pygame.image.load("Mario_Cards/Cards/A6.png")
b6 = pygame.image.load("Mario_Cards/Cards/B6.png")
c6 = pygame.image.load("Mario_Cards/Cards/C6.png")
d6 = pygame.image.load("Mario_Cards/Cards/D6.png")
a7 = pygame.image.load("Mario_Cards/Cards/A7.png")
b7 = pygame.image.load("Mario_Cards/Cards/B7.png")
c7 = pygame.image.load("Mario_Cards/Cards/C7.png")
d7 = pygame.image.load("Mario_Cards/Cards/D7.png")
a8 = pygame.image.load("Mario_Cards/Cards/A8.png")
b8 = pygame.image.load("Mario_Cards/Cards/B8.png")
c8 = pygame.image.load("Mario_Cards/Cards/C8.png")
d8 = pygame.image.load("Mario_Cards/Cards/D8.png")
a9 = pygame.image.load("Mario_Cards/Cards/A9.png")
b9 = pygame.image.load("Mario_Cards/Cards/B9.png")
c9 = pygame.image.load("Mario_Cards/Cards/C9.png")
d9 = pygame.image.load("Mario_Cards/Cards/D9.png")
a10 = pygame.image.load("Mario_Cards/Cards/A10.png")
b10 = pygame.image.load("Mario_Cards/Cards/B10.png")
c10 = pygame.image.load("Mario_Cards/Cards/C10.png")
d10 = pygame.image.load("Mario_Cards/Cards/D10.png")
a11 = pygame.image.load("Mario_Cards/Cards/A11.png")
b11 = pygame.image.load("Mario_Cards/Cards/B11.png")
c11 = pygame.image.load("Mario_Cards/Cards/C11.png")
d11 = pygame.image.load("Mario_Cards/Cards/D11.png")
a12 = pygame.image.load("Mario_Cards/Cards/A12.png")
b12 = pygame.image.load("Mario_Cards/Cards/B12.png")
c12 = pygame.image.load("Mario_Cards/Cards/C12.png")
d12 = pygame.image.load("Mario_Cards/Cards/D12.png")
a13 = pygame.image.load("Mario_Cards/Cards/A13.png")
b13 = pygame.image.load("Mario_Cards/Cards/B13.png")
c13 = pygame.image.load("Mario_Cards/Cards/C13.png")
d13 = pygame.image.load("Mario_Cards/Cards/D13.png")

#====================================================================
#                          FUNCTIONS
#====================================================================

def createCardBoard():
    cards = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13,
             14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
             27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
             40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    random.shuffle(cards)
    board = [cards[:13],
             cards[13:26],
             cards[26:39],
             cards[39:]]
    return board

def print_b(board):
    for i in board:
        print (i)

def available(board, row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def turnCard(board, row, col, player):
    board[row][col] = player

def getPoints(row, col, CARD_BOARD):
    return CARD_BOARD[row][col]

def findWinner(points):
    players = len(points)
    for player in range(0, players):
        if points[player] == max(points):
            return player + 1

def getPlayer(turn, player1, player2, player3, player4):
    if turn == 1:
        return player1
    elif turn == 2:
        return player2
    elif turn == 3:
        return player3
    else:
        return player4

def validClick(row):
    if row >= 0 and row <= 3:
        return True
    else:
        return False

#====================================================================
#                          GRAPHICS
#====================================================================

def drawBoard(window, board, CARD_BOARD, CARDS, square):
    for row in range(0, len(board)):
        for column in range(0, len(board[0])):
            pygame.draw.rect(window, white, (column * square, row * square, square, square))
            if board[row][column] == 0:
                window.blit(block, (column * square, row * square))
            else:
                value = CARD_BOARD[row][column]
                card = CARDS[value-1]
                window.blit(card, (column * square, row * square))
    pygame.display.update()

def displayText(window, text, font, color, location, width, square):
    pygame.draw.rect(window, white, (0, 400, width, square))
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = location
    window.blit(textSurface, textRect)

#====================================================================
#                          GAME LOOP
#====================================================================

def playCards(playerCount, Player1, Player2, Player3, Player4):
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13
    global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13
    global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, block

    CARD_BOARD = createCardBoard()

    BOARD = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    square = 100
    width = 13 * square
    height = 4 * square + square

    pygame.init()

    window = pygame.display.set_mode((width, height))
    window.fill(white)
    pygame.display.set_caption('Mario Cards')
    myFont = pygame.font.SysFont('Arial', 50)

    pygame.mixer.music.load("Mario_Cards/Music/Field.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    block = pygame.transform.scale(block, (square, square)).convert_alpha()
    a1 = pygame.transform.scale(a1, (square, square)).convert_alpha()
    b1 = pygame.transform.scale(b1, (square, square)).convert_alpha()
    c1 = pygame.transform.scale(c1, (square, square)).convert_alpha()
    d1 = pygame.transform.scale(d1, (square, square)).convert_alpha()
    a2 = pygame.transform.scale(a2, (square, square)).convert_alpha()
    b2 = pygame.transform.scale(b2, (square, square)).convert_alpha()
    c2 = pygame.transform.scale(c2, (square, square)).convert_alpha()
    d2 = pygame.transform.scale(d2, (square, square)).convert_alpha()
    a3 = pygame.transform.scale(a3, (square, square)).convert_alpha()
    b3 = pygame.transform.scale(b3, (square, square)).convert_alpha()
    c3 = pygame.transform.scale(c3, (square, square)).convert_alpha()
    d3 = pygame.transform.scale(d3, (square, square)).convert_alpha()
    a4 = pygame.transform.scale(a4, (square, square)).convert_alpha()
    b4 = pygame.transform.scale(b4, (square, square)).convert_alpha()
    c4 = pygame.transform.scale(c4, (square, square)).convert_alpha()
    d4 = pygame.transform.scale(d4, (square, square)).convert_alpha()
    a5 = pygame.transform.scale(a5, (square, square)).convert_alpha()
    b5 = pygame.transform.scale(b5, (square, square)).convert_alpha()
    c5 = pygame.transform.scale(c5, (square, square)).convert_alpha()
    d5 = pygame.transform.scale(d5, (square, square)).convert_alpha()
    a6 = pygame.transform.scale(a6, (square, square)).convert_alpha()
    b6 = pygame.transform.scale(b6, (square, square)).convert_alpha()
    c6 = pygame.transform.scale(c6, (square, square)).convert_alpha()
    d6 = pygame.transform.scale(d6, (square, square)).convert_alpha()
    a7 = pygame.transform.scale(a7, (square, square)).convert_alpha()
    b7 = pygame.transform.scale(b7, (square, square)).convert_alpha()
    c7 = pygame.transform.scale(c7, (square, square)).convert_alpha()
    d7 = pygame.transform.scale(d7, (square, square)).convert_alpha()
    a8 = pygame.transform.scale(a8, (square, square)).convert_alpha()
    b8 = pygame.transform.scale(b8, (square, square)).convert_alpha()
    c8 = pygame.transform.scale(c8, (square, square)).convert_alpha()
    d8 = pygame.transform.scale(d8, (square, square)).convert_alpha()
    a9 = pygame.transform.scale(a9, (square, square)).convert_alpha()
    b9 = pygame.transform.scale(b9, (square, square)).convert_alpha()
    c9 = pygame.transform.scale(c9, (square, square)).convert_alpha()
    d9 = pygame.transform.scale(d9, (square, square)).convert_alpha()
    a10 = pygame.transform.scale(a10, (square, square)).convert_alpha()
    b10 = pygame.transform.scale(b10, (square, square)).convert_alpha()
    c10 = pygame.transform.scale(c10, (square, square)).convert_alpha()
    d10 = pygame.transform.scale(d10, (square, square)).convert_alpha()
    a11 = pygame.transform.scale(a11, (square, square)).convert_alpha()
    b11 = pygame.transform.scale(b11, (square, square)).convert_alpha()
    c11 = pygame.transform.scale(c11, (square, square)).convert_alpha()
    d11 = pygame.transform.scale(d11, (square, square)).convert_alpha()
    a12 = pygame.transform.scale(a12, (square, square)).convert_alpha()
    b12 = pygame.transform.scale(b12, (square, square)).convert_alpha()
    c12 = pygame.transform.scale(c12, (square, square)).convert_alpha()
    d12 = pygame.transform.scale(d12, (square, square)).convert_alpha()
    a13 = pygame.transform.scale(a13, (square, square)).convert_alpha()
    b13 = pygame.transform.scale(b13, (square, square)).convert_alpha()
    c13 = pygame.transform.scale(c13, (square, square)).convert_alpha()
    d13 = pygame.transform.scale(d13, (square, square)).convert_alpha()

    CARDS = [a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, a4, b4, c4, d4,
             a5, b5, c5, d5, a6, b6, c6, d6, a7, b7, c7, d7, a8, b8, c8, d8,
             a9, b9, c9, d9, a10, b10, c10, d10, a11, b11, c11, d11,
             a12, b12, c12, d12, a13, b13, c13, d13]

    gameOver = False
    players = playerCount
    turn = 1
    points = []
    print_b(CARD_BOARD)
    print()
    #print_b(BOARD)
    displayText(window, Player1 + " pick a card!", myFont, black, (width/2, 450), width, square)

    while not gameOver:
        drawBoard(window, BOARD, CARD_BOARD, CARDS, square)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn <= players:
                    clickY = event.pos[1]
                    row = math.floor(clickY / square)
                    clickX = event.pos[0]
                    col = math.floor(clickX / square)
                    if validClick(row) == True:
                        if available(BOARD, row, col) == True:
                            turnCard(BOARD, row, col, turn)
                            points += [getPoints(row, col, CARD_BOARD)]
                            drawBoard(window, BOARD, CARD_BOARD, CARDS, square)
                            #print_b(BOARD)
                            turn += 1
                            player = getPlayer(turn, Player1, Player2, Player3, Player4)
                            displayText(window, player + " pick a card!", myFont, black, (width/2, 450), width, square)

                drawBoard(window, BOARD, CARD_BOARD, CARDS, square)
                if turn > players:
                    gameOver = True
                    winner = findWinner(points)
                    player = getPlayer(winner, Player1, Player2, Player3, Player4)
                    print(player + " wins memory")
                    displayText(window, player + " wins!", myFont, black, (width/2, 450), width, square)
                    pygame.display.update()
                    pygame.time.wait(3000)
    if winner == 1:
        return True
    else:
        return False