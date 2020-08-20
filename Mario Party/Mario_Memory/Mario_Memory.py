import pygame
import random
import sys
import math

#====================================================================
#                           GLOBALS
#====================================================================

white = (255,255,255)
black = (0,0,0)

memory_mario = pygame.image.load("Mario_Memory/Figures/mario.png")
memory_boo = pygame.image.load("Mario_Memory/Figures/boo.png")
memory_yoshi = pygame.image.load("Mario_Memory/Figures/yoshi.png")
memory_peach = pygame.image.load("Mario_Memory/Figures/peach.png")
memory_daisy = pygame.image.load("Mario_Memory/Figures/daisy.png")
memory_dk = pygame.image.load("Mario_Memory/Figures/dk.png")
memory_koopa = pygame.image.load("Mario_Memory/Figures/koopa.png")
memory_toad = pygame.image.load("Mario_Memory/Figures/toad.png")
memory_bowser = pygame.image.load("Mario_Memory/Figures/bowser.png")
memory_block = pygame.image.load("Mario_Memory/Figures/block.png")

#====================================================================
#                          FUNCTIONS
#====================================================================

def createCardBoard():
    cards = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    random.shuffle(cards)
    board = [cards[:6],
             cards[6:12],
             cards[12:]]
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

def checkWin(board):
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True

def checkMatch(CardBoard, row_1, col_1, row_2, col_2):
    if CardBoard[row_1][col_1] == CardBoard[row_2][col_2]:
        return True
    else:
        return False

def findWinner(board):
    counter1 = 0
    counter2 = 0
    for row in board:
        for col in row:
            if col == 1:
                counter1 += 1
            elif col == 2:
                counter2 += 1
    if counter1 > counter2:
        return 1
    else:
        return 2

def validClick(row):
    if row >= 0 and row <= 2:
        return True
    else:
        return False

#====================================================================
#                          GRAPHICS
#====================================================================

def drawBoard(window, board, CARD_BOARD, square):
    for row in range(0, len(board)):
        for column in range(0, len(board[0])):
            pygame.draw.rect(window, white, (column * square, row * square, square, square))
            if board[row][column] == 0:
                window.blit(memory_block, (column * square, row * square))
            else:
                if CARD_BOARD[row][column] == 1:
                    window.blit(memory_mario, (column * square, row * square))
                elif CARD_BOARD[row][column] == 2:
                    window.blit(memory_boo, (column * square, row * square))
                elif CARD_BOARD[row][column] == 3:
                    window.blit(memory_yoshi, (column * square, row * square))
                elif CARD_BOARD[row][column] == 4:
                    window.blit(memory_peach, (column * square, row * square))
                elif CARD_BOARD[row][column] == 5:
                    window.blit(memory_daisy, (column * square, row * square))
                elif CARD_BOARD[row][column] == 6:
                    window.blit(memory_dk, (column * square, row * square))
                elif CARD_BOARD[row][column] == 7:
                    window.blit(memory_koopa, (column * square, row * square))
                elif CARD_BOARD[row][column] == 8:
                    window.blit(memory_toad, (column * square, row * square))
                elif CARD_BOARD[row][column] == 9:
                    window.blit(memory_bowser, (column * square, row * square))

    pygame.display.update()

def displayText(window, text, font, color, location, width):
    pygame.draw.rect(window, white, (0,450, width, 100))
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = location
    window.blit(textSurface, textRect)

#====================================================================
#                          GAME LOOP
#====================================================================

def playMemory(Player1, Player2):
    global memory_mario, memory_boo, memory_yoshi, memory_peach, memory_daisy, memory_dk, memory_koopa, memory_toad, memory_bowser, memory_block

    CARD_BOARD = createCardBoard()

    BOARD = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    square = 150
    width = 6 * square
    height = 3 * square + 100

    pygame.init()

    window = pygame.display.set_mode((width, height))
    window.fill(white)
    pygame.display.set_caption('Mario Memory')
    myFont = pygame.font.SysFont('Arial', 50)

    pygame.mixer.music.load("Mario_Memory/Music/Docks.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    memory_mario = pygame.transform.scale(memory_mario, (150, 150)).convert_alpha()
    memory_boo = pygame.transform.scale(memory_boo, (150, 150)).convert_alpha()
    memory_yoshi = pygame.transform.scale(memory_yoshi, (150, 150)).convert_alpha()
    memory_peach = pygame.transform.scale(memory_peach, (150, 150)).convert_alpha()
    memory_daisy = pygame.transform.scale(memory_daisy, (150, 150)).convert_alpha()
    memory_dk = pygame.transform.scale(memory_dk, (150, 150)).convert_alpha()
    memory_koopa = pygame.transform.scale(memory_koopa, (150, 150)).convert_alpha()
    memory_toad = pygame.transform.scale(memory_toad, (150, 150)).convert_alpha()
    memory_bowser = pygame.transform.scale(memory_bowser, (150, 150)).convert_alpha()
    memory_block = pygame.transform.scale(memory_block, (150, 150)).convert_alpha()

    turn = False
    attempt = False
    gameOver = False
    print_b(CARD_BOARD)
    print()
    #print_b(BOARD)
    displayText(window, Player1 + " pick a card!", myFont, black, (width/2, 500), width)

    while not gameOver:
        drawBoard(window, BOARD, CARD_BOARD, square)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == False:
                    if attempt == False:
                        clickY = event.pos[1]
                        row_1 = math.floor(clickY / square)
                        clickX = event.pos[0]
                        col_1 = math.floor(clickX / square)
                        if validClick(row_1) == True:
                            if available(BOARD, row_1, col_1) == True:
                                turnCard(BOARD, row_1, col_1, 1)
                                drawBoard(window, BOARD, CARD_BOARD, square)
                                #print_b(BOARD)
                                attempt = not attempt
                    else:
                        clickY = event.pos[1]
                        row_2 = math.floor(clickY / square)
                        clickX = event.pos[0]
                        col_2 = math.floor(clickX / square)
                        if validClick(row_2) == True:
                            if available(BOARD, row_2, col_2) == True:
                                turnCard(BOARD, row_2, col_2, 1)
                                drawBoard(window, BOARD, CARD_BOARD, square)
                                #print_b(BOARD)
                                attempt = not attempt
                                if checkWin(BOARD) == True:
                                    gameOver = True
                                    winner = findWinner(BOARD)
                                elif checkMatch(CARD_BOARD, row_1, col_1, row_2, col_2) == False:
                                    turnCard(BOARD, row_1, col_1, 0)
                                    turnCard(BOARD, row_2, col_2, 0)
                                    turn = not turn
                                    displayText(window, Player2 + " pick a card!", myFont, black, (width/2, 500), width)
                                    pygame.time.wait(1000)

                else:
                    if attempt == False:
                        clickY = event.pos[1]
                        row_1 = math.floor(clickY / square)
                        clickX = event.pos[0]
                        col_1 = math.floor(clickX / square)
                        if validClick(row_1) == True:
                            if available(BOARD, row_1, col_1) == True:
                                turnCard(BOARD, row_1, col_1, 2)
                                drawBoard(window, BOARD, CARD_BOARD, square)
                                #print_b(BOARD)
                                attempt = not attempt
                    else:
                        clickY = event.pos[1]
                        row_2 = math.floor(clickY / square)
                        clickX = event.pos[0]
                        col_2 = math.floor(clickX / square)
                        if validClick(row_2) == True:
                            if available(BOARD, row_2, col_2) == True:
                                turnCard(BOARD, row_2, col_2, 2)
                                drawBoard(window, BOARD, CARD_BOARD, square)
                                #print_b(BOARD)
                                attempt = not attempt
                                if checkWin(BOARD) == True:
                                    gameOver = True
                                    winner = findWinner(BOARD)
                                elif checkMatch(CARD_BOARD, row_1, col_1, row_2, col_2) == False:
                                    turnCard(BOARD, row_1, col_1, 0)
                                    turnCard(BOARD, row_2, col_2, 0)
                                    turn = not turn
                                    displayText(window, Player1 + " pick a card!", myFont, black, (width/2, 500), width)
                                    pygame.time.wait(1000)
                drawBoard(window, BOARD, CARD_BOARD, square)
                #print_b(BOARD)
                if gameOver == True:
                    if winner == 1:
                        print(Player1 + " wins memory")
                        displayText(window, Player1 + " wins!", myFont, black, (width/2, 500), width)
                    else:
                        print(Player2 + " wins memory")
                        displayText(window, Player2 + " wins!", myFont, black, (width/2, 500), width)
                    pygame.display.update()
                    pygame.time.wait(3000)
    if winner == 1:
        return True
    else:
        return False
